from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Combobox")
st.caption("Search is local to the browser; choosing an option reruns Python.")

st.session_state["combobox_page_runs"] = (
    st.session_state.get("combobox_page_runs", 0) + 1
)

release = ui.combobox(
    "Release channel",
    ["Stable", "Beta", "Canary"],
    value="Stable",
    key="release-channel",
    placeholder="Search release channels",
)
topics = ui.combobox(
    "Documentation topics",
    ["Components", "Elements", "Theming", "Deployment"],
    value=["Components"],
    key="documentation-topics",
    selection_mode="multiple",
    placeholder="Search topics",
)

st.write("Selected release:", release)
st.write("Selected topics:", topics)
st.caption(f"Python runs: {st.session_state.combobox_page_runs}")

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/combobox.md").read_text()
)
