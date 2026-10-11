# LinearDS-Suite

An object-oriented Python project for learning and comparing linear data
structures. The project includes Stack, Queue, Deque, and Linked
List implementations, practical algorithms, automated tests, performance
comparisons, written analysis, and a Streamlit interface.

## Current progress: Day 6 complete — submission-ready

- Project foundation and Python package structure.
- A list-backed `Stack` with the assignment-required methods.
- A balanced-parentheses checker that uses the custom `Stack`.
- A list-backed `Queue` and FIFO task-processing simulation.
- A list-backed `Deque` and palindrome checker.
- A singly linked `LinkedList` built from `Node` objects and a task-management example.
- Automated tests for all four structures and their algorithms.
- A Streamlit interface with Home, Stack, Queue, Deque, Linked List, Algorithms, Performance, and Comparison pages.
- Session state, structure visualizations, input validation, and automated UI tests.
- Repeatable `timeit` benchmarks and saved measurements for sizes 100, 1,000, and 10,000.
- An implementation-specific Big-O comparison and approximately two-page written analysis.

Final validation passed in a clean checkout and a newly created virtual
environment: **193 tests passed**, the full benchmark completed, and all eight
Streamlit pages loaded in Chrome. Validated on Windows with Python 3.14.4,
Streamlit 1.65.0, and pytest 9.1.1. The data structures and
benchmarks use the Python standard library; the interface uses Streamlit and
the test suite uses `pytest` plus Streamlit's built-in app-testing tools.

See the [completed submission checklist](docs/submission_checklist.md) for the
requirement mapping, verification results, and final run commands. The
`v1.0-submission` Git tag identifies the final submission snapshot.

## Setup

Use Python 3.10 or newer. From the project root, create a virtual environment
and install the project dependencies:

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

## Launch the interactive app

From the project root, run:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app/app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.
If dependencies are installed in your active environment, use
`python -m streamlit run streamlit_app/app.py` instead. Stop the server with
`Ctrl+C` in its terminal.

The project configuration disables Streamlit's first-run email prompt, so
launching from the project root does not require an email address.

Choose a page in the sidebar or use the links on Home. Each structure page
lets you add values, run its required operations, view the current order,
clear the structure, and try its algorithm example. Values entered in the
structure controls are text. Blank values are rejected, and invalid operations
on empty structures show an error message.

Your objects remain available across interactions and page switches within
the same session. Refreshing the browser or starting a new session creates
fresh structures. Each user session has its own objects. Algorithm examples
use separate objects and do not change your interactive structures.
Opening a page directly also initializes the app and preserves the destination.

The Algorithms page collects all four examples. Task examples accept one
label per line, trim surrounding spaces, and ignore blank lines. The
palindrome checker compares exact characters, including case and punctuation.

The UI calls the existing classes and algorithms. Each class also provides
`to_list()`, which returns a shallow copy of its values for visualization:
bottom-to-top for Stack, front-to-rear for Queue and Deque, and node order for
Linked List. Changing the returned list does not change the structure.

The test command runs both data structure tests and UI tests. UI tests
exercise widgets through Streamlit's `AppTest`, including navigation, object
state, ordering, algorithm results, and errors.

## Performance and written comparison

Generate a new benchmark snapshot from the project root:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark
```

The benchmark saves `performance/results.json`. It runs 11 workloads at each
of three sizes, using one warm-up and five fresh trials per workload. Structure
preparation is excluded from the timing; destructive operations receive fresh
inputs for every trial. The saved file includes all samples, operation counts,
minimum trial times, averages per operation, environment information, and
source hashes. No additional benchmark dependency is needed.

For a shorter run without replacing the committed snapshot:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark --sizes 100 1000 --repeats 3 --output performance/local_results.json
```

The Performance page reads saved results and displays the Big-O table, runtime
table, and a chart. Filter by structure or switch between average cost per
operation and full-trial duration. Insertion/removal workloads use n operations;
LinkedList search uses 100 last-node probes, while deletion removes the last
node once. These distinctions matter when comparing timings. The page handles
missing or invalid results with instructions for regenerating them.

The Comparison page summarizes ordering, operations, strengths, weaknesses,
use cases, and efficiency. It also displays the written analysis in an expander.

- [Performance comparison](docs/performance_comparison.md): theoretical costs,
  measurement method, recorded results, and interpretation.
- [Written analysis](docs/analysis.md): an analytical comparison of all four structures.

The static performance report describes the committed run. Regenerating JSON
updates the UI's measurements but does not rewrite that report automatically.

## Final validation commands

After installing dependencies, run these from the project root to verify the
project without replacing the committed benchmark snapshot:

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m performance.benchmark --output performance/local_results.json
.\.venv\Scripts\python.exe -m streamlit run streamlit_app/app.py
```

The local benchmark output, virtual environments, and test caches are ignored
by Git. The committed source, tests, saved results, and reports are the
submission files; no account or email address is needed to run the app locally.

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
from datastructure_src.linked_list import LinkedList, manage_tasks

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
|-- .streamlit/
|   `-- config.toml
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
|   |-- test_linked_list.py
|   |-- test_snapshots.py
|   |-- test_performance.py
|   `-- test_streamlit_app.py
|-- performance/
|   |-- __init__.py
|   |-- benchmark.py
|   |-- comparison.py
|   `-- results.json
|-- docs/
|   |-- analysis.md
|   |-- performance_comparison.md
|   `-- submission_checklist.md
|-- streamlit_app/
|   |-- __init__.py
|   |-- app.py
|   |-- common.py
|   |-- algorithm_panels.py
|   `-- pages/
|       |-- stack_page.py
|       |-- queue_page.py
|       |-- deque_page.py
|       |-- linked_list_page.py
|       |-- algorithms_page.py
|       |-- performance_page.py
|       `-- comparison_page.py
`-- project doc/
    |-- LinearDS-Suite_README_Compact.md
    |-- DAY_01_PROJECT_SETUP_STACK.md
    |-- DAY_02_QUEUE_DEQUE.md
    |-- DAY_03_LINKED_LIST.md
    |-- DAY_04_STREAMLIT_UI.md
    |-- DAY_05_PERFORMANCE_ANALYSIS.md
    `-- DAY_06_FINAL_VALIDATION.md
```

The original [project brief](project%20doc/LinearDS-Suite_README_Compact.md),
[Day 1 plan](project%20doc/DAY_01_PROJECT_SETUP_STACK.md),
[Day 2 plan](project%20doc/DAY_02_QUEUE_DEQUE.md),
[Day 3 plan](project%20doc/DAY_03_LINKED_LIST.md),
[Day 4 plan](project%20doc/DAY_04_STREAMLIT_UI.md),
[Day 5 plan](project%20doc/DAY_05_PERFORMANCE_ANALYSIS.md), and
[Day 6 plan](project%20doc/DAY_06_FINAL_VALIDATION.md) define the project scope.
