import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Select")

choice = ui.select(options=["Apple", "Banana", "Orange"])

st.markdown(f"Currrent value: {choice}")
