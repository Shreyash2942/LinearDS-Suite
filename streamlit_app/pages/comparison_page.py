"""Summarize structure selection and present the written analysis."""

from pathlib import Path

import streamlit as st

from performance.comparison import STRUCTURE_ROWS

st.title("Structure Comparison")
st.write("Choose a structure based on the access order and operations your problem needs.")
st.dataframe([{key: row[key] for key in ("Structure", "Ordering", "Big-O")} for row in STRUCTURE_ROWS], hide_index=True, width="stretch")
st.caption("Costs apply to the current implementations. Queue and Deque use lists; LinkedList appends by walking its nodes. All four store n values in O(n) space.")

for tab, row in zip(st.tabs([row["Structure"] for row in STRUCTURE_ROWS]), STRUCTURE_ROWS):
    with tab:
        st.subheader(row["Structure"])
        st.write(f"**Ordering:** {row['Ordering']}")
        st.write(f"**Main operations:** {row['Operations']}")
        st.write(f"**Strengths:** {row['Strengths']}")
        st.write(f"**Weaknesses:** {row['Weaknesses']}")
        st.write(f"**Common use cases:** {row['Use cases']}")
        st.write(f"**Efficiency:** {row['Big-O']}")

st.info("Use Stack for newest-first access, Queue for arrival order, Deque when both ends matter, and LinkedList when an ordered node chain fits the problem. Consider the cost of locating or shifting values as the collection grows.")
with st.expander("Read the written analysis"):
    analysis_path = Path(__file__).resolve().parents[2] / "docs" / "analysis.md"
    if analysis_path.exists():
        analysis = analysis_path.read_text(encoding="utf-8")
        st.markdown(analysis.replace("(performance_comparison.md)", "(performance_page)"))
    else:
        st.info("The written analysis file is unavailable.")
