"""Interact with the custom Deque."""

import streamlit as st

from datastructure_src.deque import Deque
from streamlit_app.common import add_value, run_operation, show_sequence
from streamlit_app.algorithm_panels import palindrome_panel

st.title("Deque")
st.caption("Double-ended queue")
st.write("Add or remove values at either end. Choose the end for each operation.")
deque = st.session_state.deque
controls, view = st.columns([1, 1.3])

with controls:
    st.subheader("Operations")
    with st.form("deque_add", clear_on_submit=True):
        value = st.text_input("Value", key="deque_value", help="Values are entered as text.")
        front, rear = st.columns(2)
        if front.form_submit_button("Add front", key="deque_add_front", type="primary", width="stretch"):
            add_value(deque.addFront, value)
        if rear.form_submit_button("Add rear", key="deque_add_rear", width="stretch"):
            add_value(deque.addRear, value)

    front, rear = st.columns(2)
    if front.button("Remove front", key="deque_remove_front", width="stretch"):
        run_operation(deque.removeFront, "Removed {value} from the front.")
    if rear.button("Remove rear", key="deque_remove_rear", width="stretch"):
        run_operation(deque.removeRear, "Removed {value} from the rear.")
    if st.button("Is empty?", key="deque_empty"):
        st.info("The deque is empty." if deque.isEmpty() else "The deque is not empty.")
    if st.button("Clear deque", key="deque_clear"):
        st.session_state.deque = Deque()
        st.success("Deque cleared.")

with view:
    show_sequence(st.session_state.deque.to_list(), "Deque")

st.divider()
with st.expander("Try the palindrome checker"):
    palindrome_panel("deque_demo")
