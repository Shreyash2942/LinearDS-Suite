"""Run the four practical data structure examples."""

import streamlit as st

from streamlit_app.algorithm_panels import (
    bracket_panel,
    management_panel,
    palindrome_panel,
    processing_panel,
)

st.title("Algorithms")
st.write("See how each structure solves a practical problem.")
st.caption("Examples use their own values so your current structures stay intact.")
panels = {
    "Balanced parentheses · Stack": bracket_panel,
    "Task processing · Queue": processing_panel,
    "Palindrome checker · Deque": palindrome_panel,
    "Dynamic tasks · Linked List": management_panel,
}
example = st.selectbox("Example", list(panels), key="algorithm_example")
with st.container(border=True):
    panels[example]("algorithms_demo")
