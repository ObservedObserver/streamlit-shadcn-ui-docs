import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Tabs")

with open("docs/components/tabs.md", "r") as f:
    st.markdown(f.read())

ui.tabs(options=['PyGWalker', 'Graphic Walker', 'GWalkR', 'RATH'], defaultValue='PyGWalker', key="kanaries")

st.write(ui.tabs)
