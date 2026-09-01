# Button Group

Button Group composes related Buttons without changing the pinned shadcn
variants, dimensions, or interaction styles. It is available through
`ui.elements` because its Buttons must share one React parent.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="pagination-actions") as el:
    with el.button_group("Page actions", key="page-actions"):
        previous = el.button("Previous", key="previous", variant="outline")
        el.button_group_separator()
        el.button_group_text("Page 2 of 5")
        el.button_group_separator()
        next_page = el.button("Next", key="next", variant="outline")

st.write(previous.clicked, next_page.clicked)
```

`orientation` accepts `"horizontal"` or `"vertical"`. Direct children are
Buttons, nested Button Groups, `button_group_separator`, and
`button_group_text`. Action nodes require stable keys and retain the normal
Elements click-event behavior. Native `st.*` content cannot be placed inside
the group.
