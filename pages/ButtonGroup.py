from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Button Group")
st.caption("Related actions share one shadcn Button Group inside Elements.")

with ui.elements(key="button-group-demo") as el:
    with el.button_group("Document actions", key="document-actions"):
        previous = el.button("Previous", key="previous", variant="outline")
        el.button_group_separator()
        el.button_group_text("Page 2 of 5")
        el.button_group_separator()
        next_page = el.button("Next", key="next", variant="outline")
    with el.button_group(
        "Publish actions",
        key="publish-actions",
        orientation="vertical",
    ):
        publish = el.button("Publish", key="publish")
        el.button("Publishing", key="publishing", loading=True)

st.write(
    "Last action:",
    "previous"
    if previous.clicked
    else "next"
    if next_page.clicked
    else "publish"
    if publish.clicked
    else "none",
)

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/button_group.md").read_text()
)
