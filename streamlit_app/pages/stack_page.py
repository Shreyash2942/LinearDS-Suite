"""Interact with the custom Stack."""

import streamlit as st

from datastructure_src.stack import Stack
from streamlit_app.common import add_value, run_operation, show_sequence

st.title("Stack")
st.caption("LIFO · Last in, first out")
st.write("Push values onto the top. The most recently added value is removed first.")
stack = st.session_state.stack
controls, view = st.columns([1, 1.3])

with controls:
    st.subheader("Operations")
    with st.form("stack_add", clear_on_submit=True):
        value = st.text_input("Value", key="stack_value", help="Values are entered as text.")
        if st.form_submit_button("Push", key="stack_push", type="primary", width="stretch"):
            add_value(stack.push, value)

    pop, peek = st.columns(2)
    if pop.button("Pop", key="stack_pop", width="stretch"):
        run_operation(stack.pop, "Removed {value}.")
    if peek.button("Peek", key="stack_peek", width="stretch"):
        run_operation(stack.peek, "Top item: {value}.")
    if st.button("Is empty?", key="stack_empty"):
        st.info("The stack is empty." if stack.isEmpty() else "The stack is not empty.")
    if st.button("Clear stack", key="stack_clear"):
        st.session_state.stack = Stack()
        st.success("Stack cleared.")

with view:
    show_sequence(st.session_state.stack.to_list(), "Stack")
