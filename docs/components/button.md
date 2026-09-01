### Basic Usage

```py
import streamlit as st
import streamlit_shadcn_ui as ui

clicked = ui.button("Click")
ui.button("Reset", variant="secondary")
ui.button("Publishing", loading=True, help="Still running")
st.write("UI Button Clicked:", clicked)
```

`loading=True` adds the generated Spinner, marks the Button busy, and disables
clicks. `help=` adds a Tooltip that opens on hover or keyboard focus without a
Python rerun.
