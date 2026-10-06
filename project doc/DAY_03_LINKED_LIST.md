# Day 3 — Linked List Implementation

## Main Goal

Complete the **Linked List** portion of the project.

---

## Tasks

### 1. Create Linked List Package

Create:

```text
datastructure_src/
└── linked_list/
    ├── __init__.py
    ├── node.py
    ├── linked_list.py
    └── linked_list_algorithms.py
```

---

### 2. Implement the Node Class

File:

```text
datastructure_src/linked_list/node.py
```

Create a `Node` class with:

```python
data
next
```

Each node stores a value and a reference to the next node.

---

### 3. Implement the LinkedList Class

File:

```text
datastructure_src/linked_list/linked_list.py
```

Create a singly linked `LinkedList` class.

Required methods:

```python
insert(data)
delete(data)
search(data)
display()
```

Expected behavior:

- `insert()` adds a new node to the end,
- `delete()` removes the first matching value,
- `search()` returns `True` or `False`,
- `display()` returns a readable list representation.

Example:

```text
10 -> 20 -> 30 -> None
```

Add short class and method docstrings.

---

### 4. Create Linked List Algorithm

File:

```text
datastructure_src/linked_list/linked_list_algorithms.py
```

Implement:

**Dynamic Task / Playlist Management**

The example should use the custom `LinkedList` class to:

- add items,
- remove an item,
- search for an item,
- and display the updated sequence.

This should demonstrate how linked nodes can support a dynamic ordered collection.

---

### 5. Create Linked List Tests

Create:

```text
tests/test_linked_list.py
```

Test:

- new linked list is empty,
- first insert works,
- multiple inserts preserve order,
- search finds existing values,
- search returns `False` for missing values,
- delete removes the head,
- delete removes a middle value,
- delete removes the last value,
- delete handles a missing value,
- display returns the expected output,
- Linked List algorithm works correctly.

---

### 6. Verify Day 3

Before finishing Day 3, confirm:

- `Node` imports correctly,
- `LinkedList` imports correctly,
- all required methods work,
- Linked List algorithm works,
- Linked List tests pass,
- Stack, Queue, and Deque tests from previous days still pass.

---

## Suggested Git Commits

```text
feat: implement Node and LinkedList classes
```

```text
feat: add Linked List task management algorithm
```

```text
test: add Linked List unit tests
```

---

## Day 3 Completion Result

By the end of Day 3:

```text
Node class complete
LinkedList implementation complete
Linked List algorithm complete
Linked List tests passing
Previous data structure tests still passing
Git history updated
```

Do not begin Streamlit, performance analysis, or written analysis on Day 3.
