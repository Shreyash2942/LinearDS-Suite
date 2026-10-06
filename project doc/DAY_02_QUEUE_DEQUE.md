# Day 2 — Queue and Deque Implementation

## Main Goal

Complete the **Queue** and **Deque** portions of the project.

---

## Tasks

### 1. Create Queue Package

Create:

```text
datastructure_src/
└── queue/
    ├── __init__.py
    ├── queue.py
    └── queue_algorithms.py
```

---

### 2. Implement the Queue Class

File:

```text
datastructure_src/queue/queue.py
```

Create a `Queue` class using a Python list.

Required methods:

```python
enqueue(item)
dequeue()
front()
isEmpty()
```

Use:

```python
self._items = []
```

Expected behavior:

- `enqueue()` adds to the rear,
- `dequeue()` removes from the front,
- `front()` returns the front item without removing it,
- `isEmpty()` checks whether the queue is empty.

Use `IndexError` for invalid `dequeue()` or `front()` operations on an empty queue.

Add short class and method docstrings.

---

### 3. Create Queue Algorithm

File:

```text
datastructure_src/queue/queue_algorithms.py
```

Implement:

**Service / Task Processing Simulation**

The algorithm must use the custom `Queue` class.

Example flow:

```text
Task A enters queue
Task B enters queue
Task C enters queue

Processing order:
Task A
Task B
Task C
```

This should demonstrate FIFO behavior.

---

### 4. Create Deque Package

Create:

```text
datastructure_src/
└── deque/
    ├── __init__.py
    ├── deque.py
    └── deque_algorithms.py
```

---

### 5. Implement the Deque Class

File:

```text
datastructure_src/deque/deque.py
```

Create a `Deque` class using a Python list.

Required methods:

```python
addFront(item)
addRear(item)
removeFront()
removeRear()
isEmpty()
```

Use:

```python
self._items = []
```

Use `IndexError` when removing from an empty deque.

Add short class and method docstrings.

---

### 6. Create Deque Algorithm

File:

```text
datastructure_src/deque/deque_algorithms.py
```

Implement:

**Palindrome Checker**

The algorithm must use the custom `Deque` class.

Example:

```text
racecar
```

Expected result:

```text
Palindrome
```

---

### 7. Create Tests

Create:

```text
tests/test_queue.py
tests/test_deque.py
```

Queue tests should verify:

- new queue is empty,
- enqueue works,
- dequeue follows FIFO order,
- front returns the first item,
- front does not remove the item,
- empty dequeue raises `IndexError`,
- empty front raises `IndexError`,
- service/task algorithm works.

Deque tests should verify:

- new deque is empty,
- add to front works,
- add to rear works,
- remove from front works,
- remove from rear works,
- order is preserved,
- empty removal raises `IndexError`,
- palindrome algorithm works.

---

### 8. Verify Day 2

Before finishing Day 2, confirm:

- Queue imports correctly,
- Deque imports correctly,
- all required methods work,
- both algorithms work,
- Queue and Deque tests pass,
- Stack tests from Day 1 still pass.

---

## Suggested Git Commits

```text
feat: implement Queue data structure
```

```text
feat: add Queue processing algorithm
```

```text
feat: implement Deque data structure
```

```text
feat: add Deque palindrome algorithm
```

```text
test: add Queue and Deque unit tests
```

---

## Day 2 Completion Result

By the end of Day 2:

```text
Queue implementation complete
Queue algorithm complete
Deque implementation complete
Deque algorithm complete
Queue and Deque tests passing
Day 1 Stack tests still passing
Git history updated
```

Do not begin Linked List, Streamlit, performance analysis, or written analysis on Day 2.
