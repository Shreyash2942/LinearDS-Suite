# LinearDS-Suite

An object-oriented Python project for learning and comparing linear data
structures. The complete project will include Stack, Queue, Deque, and Linked
List implementations, practical algorithms, automated tests, performance
comparisons, written analysis, and a Streamlit interface.

## Current progress: project foundation

- Python package foundation, test dependency, and Git ignore rules.
- Original project brief and daily implementation plans.

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

## Day 1 scope

The next steps are the list-backed Stack, a balanced-parentheses checker, and
automated tests. Run the test commands above after the tests are added.

The original [project brief](project%20doc/LinearDS-Suite_README_Compact.md) and
[Day 1 plan](project%20doc/DAY_01_PROJECT_SETUP_STACK.md) define the scope.
