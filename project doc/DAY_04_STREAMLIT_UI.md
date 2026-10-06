# Day 4 — Streamlit UI Implementation

## Main Goal

Build the **Streamlit interface** and connect it to the completed Stack, Queue, Deque, and Linked List implementations.

---

## Tasks

### 1. Create Streamlit Structure

Create:

```text
streamlit_app/
├── app.py
└── pages/
    ├── stack_page.py
    ├── queue_page.py
    ├── deque_page.py
    ├── linked_list_page.py
    └── algorithms_page.py
```

---

### 2. Create Main Application

File:

```text
streamlit_app/app.py
```

Create the main Streamlit page with:

- project title,
- short project description,
- navigation to each data structure,
- brief explanation of the four structures.

Keep the home page simple and focused.

---

### 3. Create Stack Page

File:

```text
streamlit_app/pages/stack_page.py
```

Allow users to:

- push a value,
- pop a value,
- peek at the top,
- check whether the stack is empty,
- view the current stack,
- run the Balanced Parentheses example.

Use the actual custom `Stack` class.

---

### 4. Create Queue Page

File:

```text
streamlit_app/pages/queue_page.py
```

Allow users to:

- enqueue a value,
- dequeue a value,
- view the front item,
- check whether the queue is empty,
- view the current queue,
- run the Service / Task Processing example.

Use the actual custom `Queue` class.

---

### 5. Create Deque Page

File:

```text
streamlit_app/pages/deque_page.py
```

Allow users to:

- add to front,
- add to rear,
- remove from front,
- remove from rear,
- check whether the deque is empty,
- view the current deque,
- run the Palindrome Checker.

Use the actual custom `Deque` class.

---

### 6. Create Linked List Page

File:

```text
streamlit_app/pages/linked_list_page.py
```

Allow users to:

- insert a value,
- delete a value,
- search for a value,
- display the list,
- run the Dynamic Task / Playlist example.

Use the actual custom `LinkedList` class.

---

### 7. Manage Streamlit State

Use `st.session_state` so data structure objects remain available while users interact with the application.

Example idea:

```python
if "stack" not in st.session_state:
    st.session_state.stack = Stack()
```

Do not duplicate data structure logic inside the UI.

---

### 8. Verify Day 4

Before finishing Day 4, confirm:

- Streamlit application launches,
- all pages load correctly,
- buttons call the correct class methods,
- object state is preserved,
- algorithms run correctly from the UI,
- invalid operations display clear errors,
- existing unit tests still pass.

---

## Suggested Git Commits

```text
feat: add Streamlit application structure
```

```text
feat: add interactive data structure pages
```

```text
feat: connect algorithms to Streamlit UI
```

```text
fix: handle Streamlit session state and UI errors
```

---

## Day 4 Completion Result

By the end of Day 4:

```text
Streamlit application working
Stack page working
Queue page working
Deque page working
Linked List page working
Algorithms accessible from UI
Existing tests still passing
Git history updated
```

Do not begin performance benchmarking or the written analysis on Day 4.
