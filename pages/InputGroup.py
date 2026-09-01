from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Input Group")
st.caption("Serializable addons compose around the pinned shadcn input.")

st.session_state["input_group_page_runs"] = (
    st.session_state.get("input_group_page_runs", 0) + 1
)

website = ui.input_group(
    "Website",
    "docs.example.com",
    key="website-input-group",
    type="url",
    prefix="https://",
    suffix="public",
    start_icon="link",
    clearable=True,
    copyable=True,
    max_length=64,
)

st.write("Committed website:", website)
st.caption(f"Python runs: {st.session_state.input_group_page_runs}")

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/input_group.md").read_text()
)
