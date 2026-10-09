"""Interact with the custom Queue."""

import streamlit as st

from datastructure_src.queue import Queue
from streamlit_app.common import add_value, run_operation, show_sequence
from streamlit_app.algorithm_panels import processing_panel

st.title("Queue")
st.caption("FIFO · First in, first out")
st.write("Add values at the rear. Values leave from the front in arrival order.")
queue = st.session_state.queue
controls, view = st.columns([1, 1.3])

with controls:
    st.subheader("Operations")
    with st.form("queue_add", clear_on_submit=True):
        value = st.text_input("Value", key="queue_value", help="Values are entered as text.")
        if st.form_submit_button("Enqueue", key="queue_enqueue", type="primary", width="stretch"):
            add_value(queue.enqueue, value)

    remove, front = st.columns(2)
    if remove.button("Dequeue", key="queue_dequeue", width="stretch"):
        run_operation(queue.dequeue, "Removed {value}.")
    if front.button("Front", key="queue_front", width="stretch"):
        run_operation(queue.front, "Front item: {value}.")
    if st.button("Is empty?", key="queue_empty"):
        st.info("The queue is empty." if queue.isEmpty() else "The queue is not empty.")
    if st.button("Clear queue", key="queue_clear"):
        st.session_state.queue = Queue()
        st.success("Queue cleared.")

with view:
    show_sequence(st.session_state.queue.to_list(), "Queue")

st.divider()
with st.expander("Try FIFO task processing"):
    processing_panel("queue_demo")
