# Day 5 — Performance Comparison and Written Analysis

## Main Goal

Complete the **performance analysis** and the required **written comparison** of Stack, Queue, Deque, and Linked List.

---

## Tasks

### 1. Create Performance Benchmark

Create:

```text
performance/
└── benchmark.py
```

Use Python `timeit` to measure selected operations for all four data structures.

Test simple input sizes such as:

```text
100
1,000
10,000
```

Measure only meaningful operations, such as:

- Stack push/pop
- Queue enqueue/dequeue
- Deque front/rear operations
- Linked List insert/search/delete

Keep the benchmark simple and repeatable.

---

### 2. Create Performance Comparison

Create:

```text
docs/performance_comparison.md
```

Include:

- theoretical Big-O complexity,
- measured runtime results,
- explanation of why some operations are faster or slower,
- important differences caused by Python list usage,
- and a short comparison between the four structures.

Clearly separate:

```text
Theoretical Complexity
```

from:

```text
Measured Runtime
```

---

### 3. Add Performance to Streamlit

Create or complete:

```text
streamlit_app/pages/performance_page.py
```

Display:

- Big-O comparison table,
- benchmark results,
- simple performance chart,
- short explanation of the results.

The Streamlit page should read existing benchmark results instead of reimplementing data structure logic.

---

### 4. Create the Written Analysis

Create:

```text
docs/analysis.md
```

Write approximately **two pages** comparing:

- Stack,
- Queue,
- Deque,
- Linked List.

Discuss:

- how each structure works,
- strengths,
- weaknesses,
- operation efficiency,
- appropriate use cases,
- differences between the structures,
- and when each structure should be selected.

Keep the writing analytical, not only descriptive.

---

### 5. Add Structure Comparison to Streamlit

Create or complete:

```text
streamlit_app/pages/comparison_page.py
```

Show a concise comparison of:

- ordering model,
- main operations,
- strengths,
- weaknesses,
- common use cases,
- and Big-O behavior.

---

### 6. Verify Day 5

Before finishing Day 5, confirm:

- benchmark script runs successfully,
- results are reasonable,
- complexity table matches the actual implementations,
- performance page loads,
- comparison page loads,
- written analysis covers all four structures,
- all existing tests still pass.

---

## Suggested Git Commits

```text
feat: add data structure performance benchmarks
```

```text
docs: add performance comparison
```

```text
docs: add linear data structure analysis
```

```text
feat: add performance and comparison Streamlit pages
```

---

## Day 5 Completion Result

By the end of Day 5:

```text
Performance benchmark complete
Big-O comparison complete
Performance documentation complete
Two-page analysis complete
Performance Streamlit page working
Comparison Streamlit page working
Existing tests still passing
Git history updated
```

Do not add new data structures or major features on Day 5.
