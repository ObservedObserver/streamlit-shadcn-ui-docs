from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Empty")
st.caption("Empty state slots keep media, copy, and actions in one React tree.")

with ui.elements(key="empty-demo") as el:
    with el.empty(key="search-empty"):
        with el.empty_header():
            with el.empty_media(variant="icon"):
                el.spinner(label="Checking search index")
            el.empty_title("No matching components")
            el.empty_description("Clear the filters or try a broader query.")
        with el.empty_content():
            reset = el.button("Clear filters", key="clear-filters")

st.write("Clear requested:", reset.clicked)

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/empty.md").read_text()
)
