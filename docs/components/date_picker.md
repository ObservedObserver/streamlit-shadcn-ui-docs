### Basic Uage

```py
import streamlit as st
import streamlit_shadcn_ui as ui

# Date Picker
dt = ui.date_picker(key="date_picker", mode="single", label="Date Picker")
st.write("Date Value:", dt)

# Date Range Picker
dt2 = ui.date_picker(key="date_picker2", mode="range", label="Date Picker")
st.write("Date Range:", dt2)

```
