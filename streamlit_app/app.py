"""Run the LinearDS-Suite multipage Streamlit application."""

from pathlib import Path
import sys

import streamlit as st

# Streamlit starts with the entrypoint directory on its import path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from streamlit_app.common import initialize_structures


def home() -> None:
    """Introduce the four structures and link to their interactive pages."""
    st.caption("DESIGN & ANALYSIS OF ALGORITHMS")
    st.title("LinearDS-Suite")
    st.write("Explore how data moves through four linear data structures.")
    st.info("Choose a structure, add a few values, and watch how its ordering changes.")

    structures = [
        ("Stack", "Last in, first out", "The newest value leaves first, like a stack of plates.", "stack_page.py", "📚"),
        ("Queue", "First in, first out", "Values leave in arrival order, like a service line.", "queue_page.py", "🚶"),
        ("Deque", "Both ends available", "Add or remove values at the front and the rear.", "deque_page.py", "↔️"),
        ("Linked List", "A chain of nodes", "Append, find, and remove values in an ordered chain.", "linked_list_page.py", "🔗"),
    ]
    for start in (0, 2):
        columns = st.columns(2)
        for column, (name, rule, description, filename, icon) in zip(columns, structures[start:start + 2]):
            with column.container(border=True):
                st.subheader(f"{icon} {name}")
                st.caption(rule)
                st.write(description)
                st.page_link(f"pages/{filename}", label=f"Open {name}")

    st.caption("Your structures stay available as you switch pages within this session.")


st.set_page_config(page_title="LinearDS-Suite", page_icon="📚", layout="wide")
initialize_structures()
st.sidebar.title("LinearDS-Suite")
st.sidebar.caption("Explore the order of data.")
page = st.navigation([
    st.Page(home, title="Home", icon="🏠", default=True),
    st.Page("pages/stack_page.py", title="Stack", icon="📚"),
    st.Page("pages/queue_page.py", title="Queue", icon="🚶"),
    st.Page("pages/deque_page.py", title="Deque", icon="↔️"),
    st.Page("pages/linked_list_page.py", title="Linked List", icon="🔗"),
])
page.run()
