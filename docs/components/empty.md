# Empty

Empty presents a no-data or no-results state through typed header, media,
title, description, and content slots. It is available inside Elements so the
slots share the required React structure.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="empty-search") as el:
    with el.empty(key="empty"):
        with el.empty_header():
            with el.empty_media(variant="icon"):
                el.spinner(label="Checking search index")
            el.empty_title("No results")
            el.empty_description("Try another query.")
        with el.empty_content():
            reset = el.button("Clear filters", key="reset")

st.write(reset.clicked)
```

An Empty accepts at most one header and one content slot. Its header accepts
at most one media, title, and description. The content slot can hold supported
Elements actions or content. It cannot contain native `st.*` children.
