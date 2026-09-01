from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Spinner")
st.caption("Use a status spinner directly or let Button add it while loading.")

with ui.elements(key="spinner-demo") as el:
    with el.stack(gap="md"):
        el.spinner(label="Loading component data")
        el.button(
            "Publishing",
            key="publishing",
            loading=True,
            help="The publish action is still running.",
        )

ui.button(
    "Synchronizing",
    key="standalone-loading-button",
    loading=True,
    help="The synchronization is still running.",
)

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/spinner.md").read_text()
)
