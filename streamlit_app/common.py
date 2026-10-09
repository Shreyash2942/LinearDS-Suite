"""Shared state, input validation, and display helpers for the interface."""

from collections.abc import Callable
from typing import Any

import streamlit as st

from datastructure_src.deque import Deque
from datastructure_src.linked_list import LinkedList
from datastructure_src.queue import Queue
from datastructure_src.stack import Stack


def initialize_structures() -> None:
    """Create each structure once per user session."""
    for key, factory in (
        ("stack", Stack),
        ("queue", Queue),
        ("deque", Deque),
        ("linked_list", LinkedList),
    ):
        if key not in st.session_state:
            st.session_state[key] = factory()


def add_value(operation: Callable[[str], None], value: str) -> None:
    """Validate an entered value and call the structure's insertion method."""
    if not value.strip():
        st.error("Enter a value before adding it.")
        return
    operation(value)
    st.success(f"Added {value!r}.")


def run_operation(operation: Callable[[], Any], message: str) -> None:
    """Call a public operation and show its result or empty-state error."""
    try:
        value = operation()
    except IndexError as error:
        st.error(str(error))
    else:
        st.success(message.format(value=repr(value)))


def show_sequence(items: list[Any], kind: str) -> None:
    """Visualize a snapshot without changing the structure."""
    st.subheader("Current structure")
    st.metric("Items", len(items))
    if not items:
        st.info(f"The {kind.lower()} is empty. Add a value to get started.")
        return

    if kind == "Stack":
        sequence = "TOP\n" + "\n".join(f"[ {value!r} ]" for value in reversed(items))
        st.code(sequence + "\nBOTTOM", language=None)
    else:
        separator = " ↔ " if kind == "Deque" else " → "
        sequence = separator.join(repr(value) for value in items)
        st.code(f"FRONT | {sequence} | REAR", language=None)
