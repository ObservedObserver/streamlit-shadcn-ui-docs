from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Tooltip")
st.caption("Hover or focus each trigger; tooltip state stays in the browser.")

with ui.elements(key="tooltip-demo") as el:
    with el.tooltip("Runs the current release", side="top"):
        run = el.button("Run release", key="run-release")
    with el.tooltip("Open the shadcn documentation", side="right"):
        el.link_button(
            "Read documentation",
            "https://ui.shadcn.com/docs/components/base/tooltip",
            key="tooltip-docs",
        )
    with el.tooltip("Unavailable while a release is running", side="bottom"):
        el.button("Disabled action", key="disabled-action", disabled=True)

st.write("Run requested:", run.clicked)
ui.button(
    "Button help",
    key="button-help-demo",
    help="Standalone buttons can expose the same tooltip behavior.",
)

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/tooltip.md").read_text()
)
