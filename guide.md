# LinearDS-Suite User Guide

This guide explains how to install, run, explore, test, and review LinearDS-Suite. You can use the interactive application without writing Python code.

## Contents

- [What the project includes](#what-the-project-includes)
- [Download and setup](#download-and-setup)
- [Start and stop the application](#start-and-stop-the-application)
- [Using the application](#using-the-application)
- [Running the algorithms](#running-the-algorithms)
- [Performance and comparison](#performance-and-comparison)
- [Run the tests](#run-the-tests)
- [Use the classes in Python](#use-the-classes-in-python)
- [Project files and reports](#project-files-and-reports)
- [Troubleshooting](#troubleshooting)
- [Suggested project demonstration](#suggested-project-demonstration)

## What the project includes

LinearDS-Suite demonstrates four custom Python data structures:

| Structure | Ordering | Example use |
| --- | --- | --- |
| Stack | Last in, first out (LIFO) | Balanced-parentheses checking |
| Queue | First in, first out (FIFO) | Service/task processing |
| Deque | Access at both ends | Palindrome checking |
| Linked List | Ordered chain of nodes | Dynamic task/playlist management |

The project also includes an eight-page Streamlit application, automated tests, saved performance measurements, a written comparison, and a complete APA-style report. Stack, Queue, and Deque use Python lists internally; Linked List uses custom Node objects. Their actual implementation determines their operation costs.

## Download and setup

### Requirements

- Python 3.10 or newer, as specified in the README. The final project was validated with Python 3.14.4 on Windows.
- Internet access for the initial dependency installation.
- A terminal and a web browser.
- Git only if you choose to clone the repository.

No Streamlit account or email address is required to run the application locally.

### Download the project

Choose either method:

1. Open the [GitHub repository](https://github.com/Shreyash2942/LinearDS-Suite), select **Code > Download ZIP**, and extract it. Open a terminal inside the extracted folder containing `README.md` and `requirements.txt`.
2. Clone the repository from a terminal:

   ```text
   git clone https://github.com/Shreyash2942/LinearDS-Suite.git
   cd LinearDS-Suite
   ```

Use the current `main` branch for the latest guide and report. The `v1.0-submission` tag identifies the earlier validated implementation snapshot; it predates the added APA report and this guide.

All commands below must run from the **project root**, the folder containing `README.md`, `guide.md`, and `requirements.txt`.

### Windows PowerShell

Check Python, create a virtual environment, and install dependencies:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

If Windows recognizes `py` rather than `python`, use `py -m venv .venv` to create the environment. The remaining commands use the environment's Python directly.

Environment activation is optional. These commands work without activating it and avoid PowerShell activation-script restrictions. Install dependencies once for each new environment.

### macOS or Linux

```bash
python3 --version
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -m pip check
```

The remaining examples use Windows paths. On macOS/Linux, replace `.\.venv\Scripts\python.exe` with `./.venv/bin/python`.

## Start and stop the application

From the project root, run:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app/app.py
```

Open the **Local URL** printed in the terminal, normally `http://localhost:8501`. Keep that terminal running while you use the application. The project configuration disables the first-run email prompt when launched from this folder.

To stop the application, press **Ctrl+C** in the terminal. To start it another day, open a terminal in the project root and run the same launch command; you do not need to create the environment again.

## Using the application

Select a page from the sidebar or use a link on **Home**. Structure pages show the current collection and provide operation buttons. Values entered through these controls are **text**, so entering `10` stores the string `"10"`; the Python classes themselves can store other value types.

Your structures remain available across button clicks and page switches within the same browser session. Refreshing the browser, starting a new session, or restarting the server creates fresh structures. Collections are held in memory and are not saved to disk. Each browser session has its own objects.

Blank or whitespace-only values are rejected. Removing or inspecting an empty Stack or Queue, or removing from an empty Deque, displays an error. Linked List reports missing values without changing the collection.

### Home

Read the short descriptions of the four structures and select the one you want to explore. Home also links to Algorithms, Performance, and Comparison.

### Stack

1. Enter `10` in **Value** and click **Push**. Repeat for `20` and `30`.
2. Click **Peek**. The top value is `30`; the stack remains unchanged.
3. Click **Pop**. The removed value is `30`, leaving `10`, `20`.
4. Click **Is empty?** to check the collection.
5. Click **Clear stack** to reset it. Clicking **Pop** or **Peek** afterwards demonstrates the empty-stack error.

The snapshot order is bottom to top. Expand **Try balanced parentheses** for the algorithm example.

### Queue

1. Enter `Task A`, then `Task B`, then `Task C`, clicking **Enqueue** after each value.
2. Click **Front**. It shows `Task A` without removing it.
3. Click **Dequeue**. It removes `Task A`, leaving `Task B`, `Task C`.
4. Use **Is empty?** to inspect emptiness and **Clear queue** to reset the queue.

The snapshot order is front to rear. Expand **Try FIFO task processing** for the algorithm example.

### Deque

1. Enter `middle` and click **Add rear**.
2. Enter `front` and click **Add front**.
3. Enter `rear` and click **Add rear**. The sequence is now `front`, `middle`, `rear`.
4. Click **Remove front** to remove `front`.
5. Click **Remove rear** to remove `rear`, leaving `middle`.
6. Use **Is empty?** and **Clear deque** as needed.

The snapshot order is front to rear. Expand **Try the palindrome checker** for the algorithm example.

### Linked List

1. Enter `10`, `20`, and `30` in turn, clicking **Insert** for each value. Insertion appends to the end.
2. Click **Display** to see `10 -> 20 -> 30 -> None`.
3. Enter `20` and click **Search**. It reports that the value exists.
4. With `20` entered, click **Delete**. The sequence becomes `10 -> 30 -> None`.
5. Search for `99` to see the missing-value response.
6. Use **Clear list** to reset it. An empty list displays `None`.

Deletion removes only the **first matching value**. If you insert the same value twice, deleting it once leaves one occurrence. Search and delete use the entered text, including its case and spaces. Expand **Try dynamic task management** for the algorithm example.

## Running the algorithms

Use the **Algorithms** page to access all four examples, or use the expander on the corresponding structure page. Algorithm examples use separate temporary structures and do not modify the values you added on the interactive structure pages.

| Example | What to enter | Button | Expected result |
| --- | --- | --- | --- |
| Balanced parentheses | `{[()]}` | Check brackets | Balanced |
| Balanced parentheses | `([)]` | Check brackets | Not balanced |
| FIFO task processing | `Task A`, `Task B`, `Task C`, one per line | Process tasks | The same arrival order |
| Palindrome | `racecar` | Check palindrome | Palindrome |
| Palindrome | `Racecar` | Check palindrome | Not a palindrome |
| Dynamic task management | Tasks A, B, C; remove `Task B`; find `Task C` | Manage tasks | B removed; C found; A then C remain |

For the task examples, enter this in the **Tasks** box:

```text
Task A
Task B
Task C
```

Important behavior:

- Balanced parentheses checks `()`, `[]`, and `{}` nesting. It ignores other characters and treats empty input as balanced. It is not a full programming-language parser.
- FIFO processing demonstrates task **ordering**; it does not execute commands or functions supplied as task labels. Blank task lines are ignored and surrounding spaces are removed.
- Palindrome comparison is exact: case, spaces, and punctuation count. Empty text and a single character are palindromes.
- Task management removes the first matching task, then searches the updated list. Searching for the task you just removed can therefore return “not found.” The remove/find fields must contain nonblank text.

## Performance and comparison

### View existing measurements

Open **Performance** to see the Big-O table, saved runtime table, and chart. You can use it immediately after setup because `performance/results.json` is included in the repository.

- Select a **Structure** to filter measurements.
- Select **Chart measure** to switch between average time per operation in microseconds and full-trial duration in milliseconds.
- Expand **Measurement method** to review how the samples were collected.

The page reads saved results; it does not run benchmarks when opened. The default dataset contains 11 operation workloads at sizes 100, 1,000, and 10,000, giving 33 measurements. Each workload uses one warm-up and five fresh timed trials. “Average per operation” is the minimum trial time divided by the operation count, not the average of all trial samples.

Batch insertion builds a collection from empty; batch removal drains it. Linked List search makes 100 last-node probes per trial, while deletion removes the last node once. Compare these workload definitions before interpreting rankings.

### Run your own benchmark

For a shorter experiment that keeps the archived results unchanged:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark --sizes 100 1000 --repeats 3 --output performance/local_results.json
```

For the full default-size benchmark saved separately:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark --output performance/local_results.json
```

The command prints a results table and the output path. `performance/local_results.json` is ignored by Git. This separate file does **not** change the Performance page, which reads `performance/results.json`.

To deliberately update the page's saved measurements, run:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark
```

This overwrites `performance/results.json`. Reload the Performance page after it finishes. The Markdown performance comparison and APA report continue to describe the archived run; they are not automatically rewritten when JSON changes.

To inspect all command options:

```powershell
.\.venv\Scripts\python.exe -m performance.benchmark --help
```

### Understand the comparison

Open **Comparison** to review ordering, operations, strengths, weaknesses, use cases, and complexity. Expand the written analysis to read the longer discussion.

For these implementations, Stack end operations and Queue enqueue are amortized O(1). Queue dequeue and Deque front operations are O(n) because list references shift. Deque rear operations are amortized O(1). Linked List append, search, and delete are O(n) worst case because they traverse nodes; this list has no tail reference. These costs describe the project's implementations rather than every possible implementation of each structure.

## Run the tests

Run the complete suite from the project root:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Final submission validation recorded **193 passing tests**, covering the structures, algorithms, snapshots, benchmarks, and Streamlit UI. The test output from your run confirms the result in your environment. UI tests use Streamlit's AppTest and do not require starting a browser or server.

Run a single test module when reviewing a specific area:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_linked_list.py -q
.\.venv\Scripts\python.exe -m pytest tests/test_streamlit_app.py -q
```

For more detailed failure output, replace `-q` with `-v`. Dependencies can be checked with `.\.venv\Scripts\python.exe -m pip check`.

## Use the classes in Python

The core classes and algorithms use the Python standard library and can run without the Streamlit interface. Start the environment's Python interpreter from the project root:

```powershell
.\.venv\Scripts\python.exe
```

At the Python prompt, paste the following code. The comments show expected results:

```python
from datastructure_src.stack import Stack, is_balanced_parentheses
from datastructure_src.queue import Queue, process_tasks
from datastructure_src.deque import Deque, is_palindrome
from datastructure_src.linked_list import Node, LinkedList, manage_tasks

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())                    # 20; no removal
print(stack.pop())                     # 20
print(stack.to_list())                 # [10]
print(is_balanced_parentheses('{[()]}'))  # True

queue = Queue()
queue.enqueue('Task A')
queue.enqueue('Task B')
print(queue.front())                   # Task A; no removal
print(queue.dequeue())                 # Task A
print(process_tasks(['A', 'B', 'C']))   # ['A', 'B', 'C']

deque = Deque()
deque.addRear('middle')
deque.addFront('front')
deque.addRear('rear')
print(deque.removeFront())             # front
print(deque.removeRear())              # rear
print(is_palindrome('racecar'))        # True

node = Node(10)
print(node.data, node.next)            # 10 None
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
print(linked_list.search(20))           # True
print(linked_list.delete(20))           # True
print(linked_list.display())           # 10 -> None
print(manage_tasks(['A', 'B', 'C'], 'B', 'C')['updated_sequence'])
# A -> C -> None
```

Type `exit()` to leave Python. Unlike the UI, direct Python calls can store integers and other objects.

### Public method reference

| Class | Methods | Behavior |
| --- | --- | --- |
| Stack | `push(value)`, `pop()`, `peek()`, `isEmpty()` | Push returns `None`; pop removes/returns the top; peek reads it; emptiness returns a boolean. |
| Queue | `enqueue(value)`, `dequeue()`, `front()`, `isEmpty()` | Enqueue returns `None`; dequeue removes/returns the front; front reads it; emptiness returns a boolean. |
| Deque | `addFront(value)`, `addRear(value)`, `removeFront()`, `removeRear()`, `isEmpty()` | Add methods return `None`; remove methods return the removed value; emptiness returns a boolean. |
| LinkedList | `insert(value)`, `delete(value)`, `search(value)`, `display()` | Insert appends and returns `None`; delete/search return booleans; display returns a string. |
| All four | `to_list()` | Returns a shallow list snapshot in structure order. |
| Node | `data`, `next` | Stores a value and the next-node reference; a new node's next is `None`. |

Method names are case-sensitive: use `isEmpty()`, `addFront()`, and the other names exactly as shown. Empty Stack pop/peek, Queue dequeue/front, and Deque removal raise `IndexError` in direct Python use. Linked List delete returns `False` for a missing value, including on an empty list.

Snapshots are shallow: changing the returned list's membership does not alter the structure, but mutable objects inside it are still shared references.

## Project files and reports

All paths below are relative to the project root.

| Location | Purpose |
| --- | --- |
| [README.md](README.md) | Project overview, setup, progress, and implementation examples |
| [guide.md](guide.md) | This complete usage guide |
| [requirements.txt](requirements.txt) | Streamlit and pytest dependencies |
| [.streamlit/config.toml](.streamlit/config.toml) | Application theme and disabled email prompt |
| [datastructure_src/](datastructure_src/) | Custom classes and algorithm modules |
| [streamlit_app/app.py](streamlit_app/app.py) | Application entrypoint and navigation |
| [streamlit_app/pages/](streamlit_app/pages/) | Seven child pages, in addition to Home |
| [tests/](tests/) | Structure, algorithm, benchmark, and UI tests |
| [performance/benchmark.py](performance/benchmark.py) | Benchmark command-line program |
| [performance/results.json](performance/results.json) | Saved measurements displayed in the UI |
| [docs/analysis.md](docs/analysis.md) | Approximately two-page written comparison |
| [docs/performance_comparison.md](docs/performance_comparison.md) | Methodology, complexity, and archived runtime results |
| [docs/submission_checklist.md](docs/submission_checklist.md) | Academic requirement mapping and final validation |
| [docs/LinearDS_Suite_APA_Report.pdf](docs/LinearDS_Suite_APA_Report.pdf) | Complete 15-page APA-style project report |
| [docs/LinearDS_Suite_APA_Report.docx](docs/LinearDS_Suite_APA_Report.docx) | Editable report; instructor field remains blank |
| [docs/apa_report.md](docs/apa_report.md) | Report text source |

Original planning documents in `project doc/` are kept locally and ignored by Git. They are not required to install or use the current project.

## Troubleshooting

| Problem | What to do |
| --- | --- |
| `python` is not recognized on Windows | Try `py --version` and `py -m venv .venv`. If neither exists, install Python and reopen the terminal. |
| `.venv` Python path is missing | Check that the terminal is in the project root and create the environment using the setup instructions. |
| PowerShell blocks environment activation | Use the direct `.\.venv\Scripts\python.exe` commands in this guide; activation is optional. |
| `No module named streamlit` or `pytest` | Run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then use that same Python executable to launch or test. |
| `requirements.txt` or `streamlit_app/app.py` cannot be found | Change to the folder containing `README.md`. With a ZIP download, ensure you are inside the extracted project folder. |
| Import errors for `datastructure_src` or `performance` | Run from the project root and use the documented entrypoint/module commands. |
| Browser does not open automatically | Copy the Local URL from the terminal into your browser. |
| Port 8501 is already in use | Stop the existing server or launch on port 8502 using the command below. |
| An email prompt appears | Stop the server and launch from the project root so `.streamlit/config.toml` is read. |
| Values disappear after refreshing | Data is stored only for the current session. Re-enter values after a refresh or restart. |
| Empty-operation error | Add a value before removing or inspecting it. Use the emptiness button where available. |
| Linked List cannot find a value | Check case and spaces, and remember that the UI stores text and deletes only the first matching occurrence. |
| Palindrome result seems unexpected | Case, spaces, and punctuation count; `racecar` and `Racecar` have different results. |
| Performance page reports missing/invalid data | From the project root, run the default benchmark to generate `performance/results.json`, then revisit the page. |
| Local benchmark does not change the chart | The page reads `performance/results.json`, not `performance/local_results.json`. Use the default benchmark only if you intend to update the displayed dataset. |

Alternate-port launch:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app/app.py --server.port 8502
```

Then open `http://localhost:8502`.

## Suggested project demonstration

1. Launch the app and show **Home**.
2. Push three Stack values and pop one to demonstrate LIFO.
3. Enqueue three Queue values and dequeue one to demonstrate FIFO.
4. Add and remove Deque values at both ends.
5. Insert, search, delete, and display a Linked List.
6. Switch between structure pages to show that session state is preserved.
7. Run all four algorithm examples and demonstrate an empty-operation error.
8. Open **Performance** and **Comparison** to connect behavior with implementation costs.
9. Run the test command and review its summary.
10. Open the APA PDF and the submission checklist for the written analysis and validation evidence.

For submission, share the repository or an extracted project copy together with the report. Point readers to **`guide.md` in the project root** for complete usage instructions.
