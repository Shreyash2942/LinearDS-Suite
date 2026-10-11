"""Compare implementation costs with saved benchmark measurements."""

import streamlit as st

from performance.benchmark import load_results
from performance.comparison import COMPLEXITY_ROWS
from streamlit_app.common import ensure_app_context

ensure_app_context("pages/performance_page.py")
st.title("Performance")
st.write("Compare theoretical operation costs with measured runtime as input size grows.")
st.subheader("Theoretical complexity")
st.caption("n is the number of stored values; L is the number of formatted output characters. Equality comparisons are assumed constant-time.")
st.dataframe(COMPLEXITY_ROWS, hide_index=True, width="stretch")
st.caption("All four structures use O(n) storage. Amortized O(1) end operations may have an O(n) resize; front operations shift list references.")

st.subheader("Measured runtime")
try:
    saved = load_results()
except (OSError, ValueError, KeyError, TypeError) as error:
    st.error("Saved benchmark results are missing or invalid. Generate a new result file from the project root.")
    st.code(r".\.venv\Scripts\python.exe -m performance.benchmark", language=None)
    st.caption(str(error))
else:
    metadata = saved["metadata"]
    st.caption(f"Saved run: {metadata['created_at_utc']} · {metadata.get('implementation', 'Python')} {metadata['python']} · {metadata['platform']}")
    structure = st.selectbox("Structure", ["All structures", "Stack", "Queue", "Deque", "LinkedList"], key="performance_structure")
    records = [row for row in saved["results"] if structure == "All structures" or row["structure"] == structure]
    table = [{
        "Structure": row["structure"], "Operation": row["operation"], "Input size": row["n"],
        "Operations/trial": row["operations_per_trial"],
        "Best trial (ms)": row["best_seconds"] * 1_000,
        "Average/op (µs)": row["microseconds_per_operation"], "Trial Big-O": row["trial_complexity"],
    } for row in records]
    st.dataframe(table, hide_index=True, width="stretch", column_config={
        "Best trial (ms)": st.column_config.NumberColumn(format="%.6f"),
        "Average/op (µs)": st.column_config.NumberColumn(format="%.6f"),
    })

    metric = st.selectbox("Chart measure", ["Average per operation (µs)", "Full trial (ms)"], key="performance_metric")
    chart = [{
        "Input size": row["n"], "Operation": f"{row['structure']}.{row['operation']}",
        metric: row["microseconds_per_operation"] if metric.startswith("Average") else row["best_seconds"] * 1_000,
    } for row in records]
    st.line_chart(chart, x="Input size", y=metric, color="Operation", height=360)
    st.caption("Batch averages include growing or shrinking structures. LinkedList search repeatedly targets the last node; deletion removes the last node once per trial.")

    with st.expander("Measurement method"):
        st.write(f"Each case uses one warm-up and {metadata['repeats']} fresh timed trials. The table reports the minimum full-trial time, divided by the operation count for the average.")
        st.write(f"Insertion builds n values from empty; removal drains n values. Search makes {metadata['search_probes']} last-node probes; deletion removes one last node. Structure preparation is excluded, and timeit disables cyclic garbage collection during trials.")
        st.write("Python loop and method-call overhead are included. These are saved measurements from one environment; the page does not run benchmarks.")
    st.write("**Interpretation:** list-end operations have approximately constant average cost. Front operations shift references, while linked-list append, last-node search, and last-node deletion traverse the chain. Growth trends are more useful than rankings between unlike workloads.")
