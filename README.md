# LinearDS-Suite

An object-oriented Python project for learning and comparing linear data
structures. The complete project will include Stack, Queue, Deque, and Linked
List implementations, practical algorithms, automated tests, performance
comparisons, written analysis, and a Streamlit interface.

## Current progress: Day 1 complete

- Project foundation and Python package structure.
- A list-backed `Stack` with the assignment-required methods.
- A balanced-parentheses checker that uses the custom `Stack`.
- Automated tests for stack behavior, error handling, and bracket matching.

Queue, Deque, Linked List, Streamlit, benchmarks, and written analysis are
scheduled for later days. Day 1 requires only `pytest`; the implementation uses
the Python standard library.

## Setup

Use Python 3.10 or newer. From the project root, create a virtual environment
and install the test dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the tests without activating the virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

If dependencies are already installed in your active Python environment:

```text
python -m pytest -q
```

## Stack example

Run this Python code from the project root:

```python
from datastructure_src.stack import Stack, is_balanced_parentheses

stack = Stack()
stack.push(10)
stack.push(20)

print(stack.peek())     # 20; leaves the item in place
print(stack.pop())      # 20
print(stack.pop())      # 10
print(stack.isEmpty())  # True

expression = "{[()]}"
print("Balanced" if is_balanced_parentheses(expression) else "Not balanced")
```

`push(item)` returns `None`. `pop()` removes and returns the top item, and
`peek()` returns it without removal. Both `pop()` and `peek()` raise `IndexError`
on an empty stack. Each stack owns its own internal list, and callers interact
with it through the public methods.

The checker returns a boolean and supports parentheses `()`, square brackets
`[]`, and braces `{}`. It verifies matching types and nesting, ignores other
characters, and treats empty input as balanced. It checks bracket structure;
it does not parse a programming language's quoted strings or comments.

## Day 1 files

```text
LinearDS-Suite/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- datastructure_src/
|   |-- __init__.py
|   `-- stack/
|       |-- __init__.py
|       |-- stack.py
|       `-- stack_algorithms.py
|-- tests/
|   `-- test_stack.py
`-- project doc/
    |-- LinearDS-Suite_README_Compact.md
    |-- DAY_01_PROJECT_SETUP_STACK.md
    `-- ... remaining daily plans
```

The original [project brief](project%20doc/LinearDS-Suite_README_Compact.md) and
[Day 1 plan](project%20doc/DAY_01_PROJECT_SETUP_STACK.md) define the scope.
