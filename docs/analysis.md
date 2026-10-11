# Comparing Linear Data Structures in LinearDS-Suite

Selecting a linear data structure requires matching an application's access
pattern to the cost of its operations. Stack, Queue, Deque, and Linked List
all maintain collections, but they expose different ways to retrieve and
remove values. Their implementation also matters: this project uses Python
lists for the first three structures and a chain of `Node` objects for the
fourth. The discussion assumes constant-time value comparisons. It evaluates
these classes rather than treating a structure's name as a performance guarantee.

## Ordering and access

A Stack follows last-in, first-out ordering. `push()` appends to the underlying
list, `pop()` removes its final item, and `peek()` observes that item without
removal. Push and pop take amortized O(1) time, although individual resizes can
cost O(n); peek and `isEmpty()` take O(1). This makes Stack appropriate for
undo history, nested-expression matching, and depth-first traversal. Its
restricted access is useful when only the most recent unresolved item should
be considered. It is a poor choice for serving requests in arrival order or
finding an arbitrary stored item, since its API provides neither operation.

A Queue preserves first-in, first-out order. `enqueue()` adds at the rear in
amortized O(1), while `front()` reads the oldest value in O(1). However,
`dequeue()` uses `pop(0)`, requiring later references to shift and costing
O(n) in the worst case. Queue therefore expresses service fairness correctly
but becomes increasingly expensive to drain as its size grows. A task
processor or breadth-first traversal needs its ordering semantics, while a
large workload also needs an implementation with efficient front removal.
Python's documentation explains this distinction between list-end and
list-front operations. [Python data structures](https://docs.python.org/3/tutorial/datastructures.html)

A Deque permits insertion and removal at both ends. It can support either
newest-first or arrival-order access, and it fits problems such as comparing
characters from opposite ends of a word. Flexibility does not make all of
this project's operations equally fast: rear addition and removal are
amortized O(1), but `addFront()` and `removeFront()` shift list references and
are O(n). Choose this interface when both ends are essential, while recognizing
that repeated front operations limit its efficiency. Its broader API also
allows callers to violate an intended FIFO policy more easily than Queue's
restricted interface.

## Nodes, traversal, and dynamic sequences

LinkedList stores each value in a Node with a `next` reference and manages the
chain through its head. `insert()` appends by walking to the last node because
the class has no tail reference. Appending is therefore O(n) in the worst
case. `search()` and `delete()` also take O(n) when the target is last or
missing; a head match takes O(1). Deletion removes only the first equal value,
preserving later duplicates and the order of surviving nodes.

The benefit of linked storage is that unlinking a located node changes a
reference rather than shifting every following value. Nevertheless, this API
accepts a value to delete, so it must first locate the node and its predecessor.
That search prevents general deletion from being O(1). Building n values by
repeated append is O(n²) here. A dynamic playlist illustrates ordered updates
and node composition, but the present class does not automatically outperform
list-backed structures merely because the collection changes often. A tail
reference could improve append, although it would add invariants to maintain
when deleting the final node.

## Efficiency in the example algorithms

The balanced-bracket checker uses Stack effectively: for m input characters,
each bracket is pushed or popped at most once, producing O(m) time and O(m)
worst-case auxiliary storage. The Queue service example preserves task order,
but draining t tasks with repeated front removal produces O(t²) time. Similarly,
the Deque palindrome checker can require O(m²) time because it repeatedly
removes the front character. Both remain valid demonstrations of the relevant
ordering rules; their implementations explain the difference from algorithms
using constant-time operations at both ends.

The linked-list task example also exposes a workload tradeoff. Building the
sequence costs O(t²), followed by linear deletion, search, and display. These
examples show why analysis must include the operations an algorithm repeatedly
invokes, rather than assuming that a familiar algorithm has the same runtime
under every representation.

All four structures need O(n) storage, but their constant factors differ. Lists
store an array of object references and may reserve spare capacity; linked
storage allocates a separate Node for each value and follows references during
traversal. Displaying a linked list also requires time proportional to the
formatted output length, and every visualization snapshot copies n references.
The saved benchmarks isolate operation workloads from setup; they do not
measure the Streamlit interface, memory consumption, or complete application
latency. [Performance comparison](performance_comparison.md)

The practical choice begins with ordering: select Stack for newest-first work,
Queue for arrival order, Deque for access at both ends, and LinkedList for an
ordered node chain with value-based updates. Then examine frequency, input
size, and actual operation costs. The tests establish behavioral correctness,
while Big-O analysis and measured growth reveal where those correct behaviors
become expensive. Together they support a more defensible choice than either
operation names or a single timing result alone.
