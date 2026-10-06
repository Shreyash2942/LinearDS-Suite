# Day 1 — Project Setup and Stack Implementation

## Main Goal

Set up the project foundation and complete the **Stack** portion of the project.

---

## Tasks

### 1. Create Project Structure

Create the main folders and package files needed for the project.

Focus on:

```text
datastructure_src/
└── stack/
    ├── __init__.py
    ├── stack.py
    └── stack_algorithms.py

tests/
└── test_stack.py
```

Also create:

```text
README.md
requirements.txt
.gitignore
```

---

### 2. Implement the Stack Class

File:

```text
datastructure_src/stack/stack.py
```

Create a `Stack` class using a Python list.

Required methods:

```python
push(item)
pop()
peek()
isEmpty()
```

Use an internal list such as:

```python
self._items = []
```

Use `IndexError` for invalid `pop()` or `peek()` operations on an empty stack.

Add short class and method docstrings.

---

### 3. Create the Stack Algorithm

File:

```text
datastructure_src/stack/stack_algorithms.py
```

Implement:

**Balanced Parentheses Checker**

The algorithm must use the custom `Stack` class.

Example input:

```text
{[()]}
```

Expected result:

```text
Balanced
```

---

### 4. Create Stack Tests

File:

```text
tests/test_stack.py
```

Test:

- new stack is empty,
- `push()` adds items,
- `peek()` returns the top item,
- `pop()` follows LIFO order,
- `peek()` does not remove an item,
- empty `pop()` raises `IndexError`,
- empty `peek()` raises `IndexError`,
- balanced-parentheses algorithm works correctly.

---

### 5. Verify Day 1

Before finishing Day 1, confirm:

- Stack class imports correctly,
- all required methods work,
- Stack algorithm works,
- all Stack tests pass,
- no unnecessary files or dependencies were added.

---

## Suggested Git Commits

```text
chore: initialize LinearDS-Suite project structure
```

```text
feat: implement Stack data structure
```

```text
feat: add Stack balanced-parentheses algorithm
```

```text
test: add Stack unit tests
```

---

## Day 1 Completion Result

By the end of Day 1:

```text
Project foundation complete
Stack implementation complete
Stack algorithm complete
Stack tests passing
Git history updated
```

Do not begin Queue, Deque, Linked List, Streamlit, or performance work on Day 1.
