# Performance Comparison

This report evaluates the custom classes in `datastructure_src`. It describes
their current implementations and the saved benchmark snapshot, rather than
assuming that all implementations of a named structure have identical costs.

## Theoretical Complexity

Here, n is the number of stored values. Equality comparisons are assumed O(1),
and L is the length of a formatted display. Amortized costs describe a sequence
of operations; an individual list resize or shrink can still cost O(n).

| Structure | Operation | Time | Implementation detail |
|---|---|---|---|
| Stack | push | O(1) amortized | A resize can cost O(n). |
| Stack | pop | O(1) amortized | A list shrink can cost O(n). |
| Stack | peek / isEmpty | O(1) | Read the last item or list length. |
| Queue | enqueue | O(1) amortized | Append at the rear; resize can cost O(n). |
| Queue | dequeue | O(n) worst case | pop(0) shifts the remaining references. |
| Queue | front / isEmpty | O(1) | Read index zero or list length. |
| Deque | addFront / removeFront | O(n) worst case | Front insertion/removal shifts references. |
| Deque | addRear / removeRear | O(1) amortized | End operations; resizing can cost O(n). |
| Deque | isEmpty | O(1) | Check list length. |
| LinkedList | insert | O(n) worst case | Walk to the end; empty-list insertion is O(1). No tail reference. |
| LinkedList | search / delete | O(n) worst case | Locate the first match; a head match is O(1). |
| LinkedList | display | O(n + L) | Visit n nodes and format L output characters (assuming simple values). |
| All four | to_list | O(n) | Copy or traverse n references into a shallow snapshot. |

All four structures use O(n) storage. `to_list()` allocates an additional O(n)
shallow snapshot. LinkedList display requires O(n + L) time and temporary
storage for formatted strings; arbitrary user-defined formatting or equality
methods can add costs beyond the assumptions above.

The batch costs differ from individual-operation costs. Building n items with
Stack push, Queue enqueue, or Deque rear addition takes O(n) amortized time;
building with Deque front addition or LinkedList append takes O(n²). Draining
the list-backed front takes O(n²), whereas draining the rear takes O(n)
amortized time. Performing p full-length linked-list searches costs O(pn);
deleting one last node costs O(n).

## Measured Runtime

Run from the project root:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark
```

The default inputs are 100, 1,000, and 10,000 distinct integers. Each case has
one untallied warm-up followed by five timed trials. `timeit.Timer` rebuilds
the structure in its setup callback before every trial, with `number=1` so
destructive workloads never reuse drained state. Preparation, file output,
and UI rendering are excluded. Python loops, method calls, node allocation
during insertion, and reference handling during removal are included.

The report uses the minimum repeated full-trial time as a lower-bound estimate,
following Python's `timeit` guidance. Cyclic garbage collection is disabled
during trials by `timeit`; this does not remove normal reference-counting costs.
All five raw samples are retained in the JSON, so the minimum is not presented
as a statistical confidence interval. [Python timeit documentation](https://docs.python.org/3/library/timeit.html)

Recorded at **2026-10-10T23:23:02.635836+00:00**, using **CPython 3.14.4** on **Windows-11-10.0.26300-SP0**.

**Reported units: microseconds per operation**, computed as the best full-trial
time divided by that trial's operation count.

| Structure | Operation / workload | n = 100 | n = 1,000 | n = 10,000 |
|---|---|---:|---:|---:|
| Stack | push: build n items | 0.034000 | 0.032500 | 0.029350 |
| Stack | pop: drain n items | 0.060000 | 0.054400 | 0.052620 |
| Queue | enqueue: build n items | 0.034000 | 0.032100 | 0.028710 |
| Queue | dequeue: drain n items | 0.068000 | 0.085800 | 0.305860 |
| Deque | addFront: build n items | 0.057000 | 0.158100 | 1.039570 |
| Deque | addRear: build n items | 0.034000 | 0.037100 | 0.028170 |
| Deque | removeFront: drain n items | 0.069000 | 0.085600 | 0.307030 |
| Deque | removeRear: drain n items | 0.055000 | 0.054300 | 0.051990 |
| LinkedList | insert: build n items | 0.594000 | 4.326500 | 40.303710 |
| LinkedList | search: 100 last-node searches | 1.601000 | 13.844000 | 254.983000 |
| LinkedList | delete: one last-node deletion | 2.100016 | 17.000013 | 265.099981 |

Insertion cases add n values to an initially empty structure. Removal cases
remove all n preloaded values, so their average spans shrinking sizes. Search
targets the last value of an n-node list 100 times per trial, keeping its size
constant. LinkedList deletion removes the last value exactly once from a fresh
n-node list. Therefore the search and deletion rows measure full-length scans,
while insertion/removal rows are batch averages rather than measurements of
one operation on a permanently fixed-size collection.

The complete trial durations, operation counts, raw samples, environment, and
source-file hashes are stored in [results.json](../performance/results.json).
The Streamlit page reads this file without executing the benchmark. This
document describes the recorded run above; rerunning the command replaces
the JSON snapshot but does not automatically rewrite this static report.

## Interpreting the Results

At n = 10,000, building the Stack took 0.293500 ms, while building the LinkedList took 403.037100 ms. The Stack appends at the list end; LinkedList walks an increasingly long chain for each insertion. The corresponding batch-average costs remain nearly constant for Stack and increase substantially for LinkedList.

Draining 10,000 queued values took 3.058600 ms, compared with 0.526200 ms for Stack pop. These operations implement different ordering policies, but the growing gap illustrates the cost of shifting references at the front. LinkedList last-node searches and deletion also grow with n because each traverses the chain. These observations are consistent with the source-code analysis; the measurements alone do not establish the bounds.

Python lists make the distinction between front and rear operations decisive.
Insertion or removal at index zero shifts references, whereas the end avoids
that shifting. Queue and Deque therefore have meaningful ordering interfaces
but share the same front-removal cost in this project. Moving references inside
the list can still be faster in absolute time than traversing Python Node
objects; equal Big-O bounds do not imply equal runtimes. [Python list and queue guidance](https://docs.python.org/3/tutorial/datastructures.html)

LinkedList deletion must locate both the value and its predecessor before
rewiring the chain. Only the final reference update is constant-time. Likewise,
the absence of a tail reference makes repeated append quadratic. These are
implementation-specific costs, not universal properties of every linked list.

Small timings include timer and callable overhead, and the single-deletion
case is especially sensitive to scheduling noise. The tests deliberately make
no assertions about speed rankings or timing thresholds. Three input sizes on
one machine support a growth comparison, not a proof of asymptotic complexity
or a guarantee of production latency. No memory benchmark was performed.

## Choosing Between the Structures

Stack fits newest-first access with inexpensive end operations. Queue fits
arrival-order processing, while its current front removal limits large drains.
Deque fits workflows requiring both ends, with higher costs at the front in
this list-backed version. LinkedList fits ordered node updates and composition,
but value lookup and append require traversal. Choose the necessary access
policy first, then evaluate the implementation against the expected workload.
