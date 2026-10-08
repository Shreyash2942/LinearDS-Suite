# LinearDS-Suite

An object-oriented Python project for learning and comparing linear data
structures. The complete project will include Stack, Queue, Deque, and Linked
List implementations, practical algorithms, automated tests, performance
comparisons, written analysis, and a Streamlit interface.

## Current progress: Day 3 complete

- Project foundation and Python package structure.
- A list-backed `Stack` with the assignment-required methods.
- A balanced-parentheses checker that uses the custom `Stack`.
- A list-backed `Queue` and FIFO task-processing simulation.
- A list-backed `Deque` and palindrome checker.
- A singly linked `LinkedList` built from `Node` objects and a task-management example.
- Automated tests for all four structures and their algorithms.

Streamlit, benchmarks, and written analysis are scheduled for later days.
Days 1 through 3 require only `pytest`; the implementation uses
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

## Queue example

```python
from datastructure_src.queue import Queue, process_tasks

queue = Queue()
queue.enqueue("Task A")
queue.enqueue("Task B")

print(queue.front())    # Task A; leaves the item in place
print(queue.dequeue()) # Task A
print(queue.dequeue()) # Task B
print(queue.isEmpty()) # True

print(process_tasks(["Task A", "Task B", "Task C"]))
# ['Task A', 'Task B', 'Task C']
```

`enqueue(item)` returns `None`. `dequeue()` removes and returns the front item,
and `front()` returns it without removal. Both `dequeue()` and `front()` raise
`IndexError` on an empty queue. `process_tasks()` accepts an iterable, enqueues
the tasks, and returns them in FIFO processing order. It preserves task values
and does not execute them. Empty input returns an empty list.

## Deque example

```python
from datastructure_src.deque import Deque, is_palindrome

deque = Deque()
deque.addRear("middle")
deque.addFront("front")
deque.addRear("rear")

print(deque.removeFront()) # front
print(deque.removeRear())  # rear
print(deque.removeFront()) # middle
print(deque.isEmpty())     # True

text = "racecar"
print("Palindrome" if is_palindrome(text) else "Not a palindrome")
```

`addFront(item)` and `addRear(item)` return `None`. `removeFront()` and
`removeRear()` remove and return an item from the indicated end and raise
`IndexError` when the deque is empty. The front is index zero of the internal
list; the rear is the end. Queue and Deque instances each own their storage.

`is_palindrome()` compares characters exactly, including case, spaces, and
punctuation. For example, `racecar` is a palindrome, while `Racecar` and
`racecar!` are not. Empty text and single characters are palindromes. The
algorithm uses the custom Deque to compare characters from opposite ends.

## Linked List example

```python
from datastructure_src.linked_list import LinkedList, Node, manage_tasks

linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

print(linked_list.display())  # 10 -> 20 -> 30 -> None
print(linked_list.search(20)) # True
print(linked_list.delete(20)) # True
print(linked_list.display())  # 10 -> 30 -> None

result = manage_tasks(["Task A", "Task B", "Task C"], "Task B", "Task C")
print(result["initial_sequence"]) # Task A -> Task B -> Task C -> None
print(result["removed"])          # True
print(result["found"])            # True
print(result["updated_sequence"]) # Task A -> Task C -> None
```

Each `Node` has `data` and `next` attributes. A new node's `next` is `None`.
`LinkedList` manages a chain of nodes through its internal head reference.
`insert(data)` appends a node and returns `None`. `delete(data)` removes the
first value equal to `data` and returns `True`; it returns `False` when the
value is missing, including on an empty list. Duplicates after the first match
remain in the list. `search(data)` returns a boolean without changing the list.

`display()` returns a string ending in `None`; an empty list returns `"None"`.
It does not print. All values, including `None`, can be stored in nodes.
`manage_tasks()` adds the supplied tasks in order, removes one matching task,
searches the updated list, and returns the initial and updated sequences plus
the removal and search results. It leaves the input collection unchanged.

## Current files

```text
LinearDS-Suite/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- datastructure_src/
|   |-- __init__.py
|   |-- stack/
|   |   |-- __init__.py
|   |   |-- stack.py
|   |   `-- stack_algorithms.py
|   |-- queue/
|   |   |-- __init__.py
|   |   |-- queue.py
|   |   `-- queue_algorithms.py
|   |-- deque/
|   |   |-- __init__.py
|   |   |-- deque.py
|   |   `-- deque_algorithms.py
|   `-- linked_list/
|       |-- __init__.py
|       |-- node.py
|       |-- linked_list.py
|       `-- linked_list_algorithms.py
|-- tests/
|   |-- test_stack.py
|   |-- test_queue.py
|   |-- test_deque.py
|   `-- test_linked_list.py
`-- project doc/
    |-- LinearDS-Suite_README_Compact.md
    |-- DAY_01_PROJECT_SETUP_STACK.md
    |-- DAY_02_QUEUE_DEQUE.md
    |-- DAY_03_LINKED_LIST.md
    `-- ... remaining daily plans
```

The original [project brief](project%20doc/LinearDS-Suite_README_Compact.md),
[Day 1 plan](project%20doc/DAY_01_PROJECT_SETUP_STACK.md),
[Day 2 plan](project%20doc/DAY_02_QUEUE_DEQUE.md), and
[Day 3 plan](project%20doc/DAY_03_LINKED_LIST.md) define the current scope.
