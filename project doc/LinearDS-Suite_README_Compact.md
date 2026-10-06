# LinearDS-Suite

## Project Overview

**LinearDS-Suite** is an object-oriented Python project that implements and demonstrates four linear data structures:

- Stack
- Queue
- Deque
- Linked List

The project includes required data structure operations, practical algorithms, automated tests, performance comparison, written analysis, and an interactive **Streamlit UI** for visualization and demonstration.

The main goal is to satisfy the academic milestone requirements while also making the data structures easy to understand and interact with.

---

## Project Objectives

The project will:

- implement Stack, Queue, Deque, and Linked List,
- use Python classes and objects,
- demonstrate OOP concepts such as encapsulation, abstraction, and composition,
- create algorithms showing appropriate use cases,
- test all required operations,
- compare theoretical and measured performance,
- provide a two-page written comparison,
- and build a Streamlit interface for interactive demonstrations.

---

## Required Data Structures

### Stack

Implemented using a Python list.

Required methods:

```python
push(item)
pop()
peek()
isEmpty()
```

Behavior: **LIFO — Last In, First Out**

Example use case: Balanced Parentheses Checker.

### Queue

Implemented using a Python list.

Required methods:

```python
enqueue(item)
dequeue()
front()
isEmpty()
```

Behavior: **FIFO — First In, First Out**

Example use case: Service or Task Processing Simulation.

### Deque

Implemented using a Python list.

Required methods:

```python
addFront(item)
addRear(item)
removeFront()
removeRear()
isEmpty()
```

Example use case: Palindrome Checker.

### Linked List

Implemented as a singly linked list using `Node` objects.

Required methods:

```python
insert(data)
delete(data)
search(data)
display()
```

Example use case: Dynamic Task or Playlist Management.

---

## Object-Oriented Design

The project will use:

- classes,
- objects,
- constructors,
- instance methods,
- encapsulation,
- abstraction,
- composition.

Main classes:

```text
Stack
Queue
Deque
Node
LinkedList
```

Example:

```python
stack = Stack()
stack.push(10)
stack.push(20)
```

Internal list-based structures will use an attribute such as:

```python
self._items = []
```

Users will interact through public class methods instead of directly modifying internal storage.

The Linked List will demonstrate composition because a `LinkedList` object manages multiple `Node` objects.

---

## Project Structure

```text
LinearDS-Suite/
│
├── README.md
├── requirements.txt
│
├── datastructure_src/
│   ├── stack/
│   │   ├── __init__.py
│   │   ├── stack.py
│   │   └── stack_algorithms.py
│   │
│   ├── queue/
│   │   ├── __init__.py
│   │   ├── queue.py
│   │   └── queue_algorithms.py
│   │
│   ├── deque/
│   │   ├── __init__.py
│   │   ├── deque.py
│   │   └── deque_algorithms.py
│   │
│   └── linked_list/
│       ├── __init__.py
│       ├── node.py
│       ├── linked_list.py
│       └── linked_list_algorithms.py
│
├── tests/
│   ├── test_stack.py
│   ├── test_queue.py
│   ├── test_deque.py
│   └── test_linked_list.py
│
├── performance/
│   └── benchmark.py
│
├── streamlit_app/
│   ├── app.py
│   └── pages/
│
└── docs/
    ├── analysis.md
    └── performance_comparison.md
```

---

## Streamlit Application

The Streamlit UI will allow users to interact with each data structure and see how operations affect the structure.

Planned sections:

```text
Home
Stack
Queue
Deque
Linked List
Algorithms
Performance
Comparison
```

Users will be able to:

- add and remove values,
- run required operations,
- see the current structure,
- run practical algorithms,
- view Big-O complexity,
- and compare performance between structures.

Streamlit will use the actual classes and algorithms from each package under `datastructure_src`; the UI will not duplicate the data structure logic.

---

## Algorithms

Each data structure will have one main problem-solving example:

| Structure | Algorithm / Use Case |
|---|---|
| Stack | Balanced Parentheses |
| Queue | Service / Task Processing |
| Deque | Palindrome Checker |
| Linked List | Dynamic Task / Playlist |

These examples demonstrate why each structure is appropriate for a different type of problem.

---

## Testing

Each structure will have separate automated tests.

Tests will verify:

- object creation,
- required methods,
- insertion and removal,
- correct ordering,
- empty-state behavior,
- search and delete behavior,
- error handling,
- and expected return values.

---

## Performance Analysis

The project will compare both:

- theoretical Big-O complexity,
- measured runtime using Python `timeit`.

The performance section will explain why operations differ between structures and will display comparison results through Streamlit.

---

## Written Analysis

A two-page written analysis will compare:

- how each structure works,
- strengths and weaknesses,
- operation efficiency,
- appropriate use cases,
- and when one structure should be selected over another.

---

## Technologies

- Python 3
- Streamlit
- `pytest` or `unittest`
- Python `timeit`
- Git / GitHub
- Markdown

---

## Coding Standards

The project will follow:

- clear class and method names,
- docstrings,
- meaningful variables,
- modular code,
- separation between implementation, tests, algorithms, UI, and documentation,
- and assignment-required method names.

Required names such as `isEmpty()`, `addFront()`, and `removeRear()` will remain unchanged to match the assignment.

---

## Completion Criteria

The project is complete when:

- all four data structures work correctly,
- all required methods are implemented,
- classes and objects are used properly,
- automated tests pass,
- each structure has an appropriate algorithm example,
- Streamlit demonstrations work,
- performance comparison is complete,
- the two-page analysis is complete,
- and all academic milestone requirements are satisfied.

---

## Scope

The first version is a **submission-level project**.

It will focus on the academic requirements plus the Streamlit visualization.

Features such as databases, APIs, authentication, cloud deployment, and other advanced portfolio features are intentionally excluded from the initial version.

After submission, the same project can be expanded into a stronger portfolio project.
