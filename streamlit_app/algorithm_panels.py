"""Reusable forms that call the project's example algorithms."""

import streamlit as st

from datastructure_src.deque import is_palindrome
from datastructure_src.linked_list import manage_tasks
from datastructure_src.queue import process_tasks
from datastructure_src.stack import is_balanced_parentheses


def bracket_panel(prefix: str) -> None:
    """Run the balanced-parentheses checker on entered text."""
    st.caption("Match (), [], and {} in the correct order. Other characters are ignored.")
    with st.form(f"{prefix}_form"):
        expression = st.text_input("Expression", value="{[()]}", key=f"{prefix}_expression")
        submitted = st.form_submit_button("Check brackets", key=f"{prefix}_run", type="primary")
    if submitted:
        if is_balanced_parentheses(expression):
            st.success("Balanced")
        else:
            st.warning("Not balanced: a bracket is missing, mismatched, or out of order.")


def processing_panel(prefix: str) -> None:
    """Run a FIFO service simulation on task labels."""
    st.caption("Enter one task per line. Blank lines are ignored; surrounding spaces are removed.")
    with st.form(f"{prefix}_form"):
        text = st.text_area("Tasks", value="Task A\nTask B\nTask C", key=f"{prefix}_tasks")
        submitted = st.form_submit_button("Process tasks", key=f"{prefix}_run", type="primary")
    if submitted:
        tasks = [line.strip() for line in text.splitlines() if line.strip()]
        processed = process_tasks(tasks)
        if processed:
            st.success("Tasks processed in arrival order.")
            st.code(" → ".join(processed), language=None)
        else:
            st.info("No tasks to process. Enter a task on its own line.")


def palindrome_panel(prefix: str) -> None:
    """Run the palindrome checker with its exact-character semantics."""
    st.caption("Case, spaces, and punctuation count. Empty text is a palindrome.")
    with st.form(f"{prefix}_form"):
        text = st.text_input("Text", value="racecar", key=f"{prefix}_text")
        submitted = st.form_submit_button("Check palindrome", key=f"{prefix}_run", type="primary")
    if submitted:
        if is_palindrome(text):
            st.success("Palindrome")
        else:
            st.warning("Not a palindrome")


def management_panel(prefix: str) -> None:
    """Add, remove, search, and display a dynamic task list."""
    st.caption("Enter one task per line. Search runs after the first matching task is removed.")
    with st.form(f"{prefix}_form"):
        text = st.text_area("Tasks", value="Task A\nTask B\nTask C", key=f"{prefix}_tasks")
        remove = st.text_input("Task to remove", value="Task B", key=f"{prefix}_remove")
        find = st.text_input("Task to find", value="Task C", key=f"{prefix}_find")
        submitted = st.form_submit_button("Manage tasks", key=f"{prefix}_run", type="primary")
    if submitted:
        if not remove.strip() or not find.strip():
            st.error("Enter both a task to remove and a task to find.")
            return
        tasks = [line.strip() for line in text.splitlines() if line.strip()]
        result = manage_tasks(tasks, remove.strip(), find.strip())
        st.write("**Initial sequence**")
        st.code(result["initial_sequence"], language=None)
        if result["removed"]:
            st.success(f"Removed the first occurrence of {remove.strip()!r}.")
        else:
            st.warning(f"{remove.strip()!r} was not found; no task was removed.")
        if result["found"]:
            st.success(f"Found {find.strip()!r} in the updated list.")
        else:
            st.info(f"{find.strip()!r} was not found in the updated list.")
        st.write("**Updated sequence**")
        st.code(result["updated_sequence"], language=None)
