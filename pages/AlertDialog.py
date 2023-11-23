import streamlit as st
import streamlit_shadcn_ui as ui

st.subheader("Alert Dialog")
st.text("Alert Dialogs are used to display information to the user. It is a modal window, blocking other actions in the application until it is closed.")
trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog_1")