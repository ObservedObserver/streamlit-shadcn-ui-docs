# Dialog

Dialog is an Elements-only modal composition. Its trigger, content, footer,
focus trap, Escape handling, and return focus live in the shared component
ShadowRoot. Opening and dismissing the overlay do not rerun Python.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="profile-dialog") as el:
    with el.dialog(
        "Edit profile",
        key="dialog",
        description="Review the details before closing.",
        trigger_label="Open profile dialog",
    ):
        name = el.input("Display name", "Ada", key="name")
        with el.dialog_footer():
            save = el.button("Save without closing", key="save")
            done = el.dialog_close_button("Done", key="done")

st.write(name.value, save.clicked, done.clicked)
```

A regular footer Button dispatches its Elements action and leaves the Dialog
open across that rerun. `dialog_close_button` closes first, then dispatches its
action. At most one footer is allowed. Dialog content can contain supported
Elements nodes, but not arbitrary native `st.*` commands. Use `alert_dialog`
when Python must explicitly request a destructive confirmation.
