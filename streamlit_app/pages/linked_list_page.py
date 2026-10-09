"""Interact with the custom LinkedList."""

import streamlit as st

from datastructure_src.linked_list import LinkedList
from streamlit_app.common import add_value

st.title("Linked List")
st.caption("An ordered chain of nodes")
st.write("Append values at the end, search the chain, or delete the first matching value.")
linked_list = st.session_state.linked_list
controls, view = st.columns([1, 1.3])

with controls:
    st.subheader("Operations")
    with st.form("linked_list_actions"):
        value = st.text_input("Value", key="linked_list_value", help="Values are entered as text.")
        insert, delete, search = st.columns(3)
        if insert.form_submit_button("Insert", key="linked_list_insert", type="primary", width="stretch"):
            add_value(linked_list.insert, value)
        if delete.form_submit_button("Delete", key="linked_list_delete", width="stretch"):
            if not value.strip():
                st.error("Enter a value to delete.")
            elif linked_list.delete(value):
                st.success(f"Deleted the first occurrence of {value!r}.")
            else:
                st.warning(f"{value!r} was not found; the list is unchanged.")
        if search.form_submit_button("Search", key="linked_list_search", width="stretch"):
            if not value.strip():
                st.error("Enter a value to search for.")
            elif linked_list.search(value):
                st.success(f"Found {value!r}.")
            else:
                st.info(f"{value!r} was not found.")

    if st.button("Display", key="linked_list_display"):
        st.code(linked_list.display(), language=None)
    if st.button("Clear list", key="linked_list_clear"):
        st.session_state.linked_list = LinkedList()
        st.success("Linked list cleared.")

with view:
    current = st.session_state.linked_list
    st.subheader("Current structure")
    st.metric("Items", len(current.to_list()))
    st.code(current.display(), language=None)
    if not current.to_list():
        st.info("The linked list is empty. Insert a value to get started.")
