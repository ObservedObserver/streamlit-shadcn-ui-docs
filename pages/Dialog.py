from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Dialog")
st.caption("The open state and focus trap stay in the shared browser overlay.")

with ui.elements(key="dialog-demo") as el:
    with el.dialog(
        "Edit profile",
        key="profile-dialog",
        description="Review these details before closing the dialog.",
        trigger_label="Open profile dialog",
    ):
        name = el.input("Display name", "Ada", key="display-name")
        el.text(
            "Save without closing reruns Python while the dialog remains open.",
            variant="muted",
        )
        with el.dialog_footer():
            save = el.button("Save without closing", key="save")
            close = el.dialog_close_button("Done", key="done")

st.write("Display name:", name.value)
st.write("Dialog action:", "save" if save.clicked else "done" if close.clicked else "none")

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/dialog.md").read_text()
)
