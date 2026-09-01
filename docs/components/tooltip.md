# Tooltip

Tooltip reveals concise help on hover or keyboard focus. It is an Elements
composition with exactly one Button or Link Button trigger. Its open state is
local and does not rerun Python.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="tooltips") as el:
    with el.tooltip("Runs the current release", side="top"):
        run = el.button("Run release", key="run")
    with el.tooltip("Unavailable during publishing", side="bottom"):
        el.button("Disabled action", key="disabled", disabled=True)

ui.button("Button help", help="Standalone Button tooltip")
st.write(run.clicked)
```

`side` accepts `"top"`, `"right"`, `"bottom"`, or `"left"`. Disabled
triggers receive a focusable wrapper so keyboard users can still reach their
help. Standalone Buttons expose the same behavior through `help=`. Tooltip
content is plain text and cannot contain arbitrary `st.*` children.
