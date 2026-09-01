# Spinner

Spinner communicates an in-progress state. The standalone Button API can add
it automatically; a standalone Spinner is available inside Elements with an
accessible status label.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="loading-state") as el:
    el.spinner(label="Loading component data")
    el.button("Publishing", key="publishing", loading=True)

ui.button("Synchronizing", loading=True, help="Still running")
st.write("The loading buttons are disabled while busy.")
```

`el.spinner(label=...)` is a local display node and does not rerun Python.
`loading=True` adds the generated Spinner to a Button, sets `aria-busy`, and
disables the action. No progress percentage is implied; use `ui.progress` for
determinate work.
