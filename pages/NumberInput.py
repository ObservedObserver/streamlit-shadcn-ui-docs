from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Number Input")
st.caption("Type a value or use the decrement and increment buttons.")

if "number_input_changes" not in st.session_state:
    st.session_state.number_input_changes = 0


def record_quantity_change() -> None:
    st.session_state.number_input_changes += 1


quantity = ui.number_input(
    "Quantity",
    value=1,
    min_value=1,
    max_value=10,
    key="number-input-quantity",
    on_change=record_quantity_change,
)
st.write("Quantity:", quantity)
st.caption(f"Quantity changes: {st.session_state.number_input_changes}")

threshold = ui.number_input(
    "Threshold",
    value=0.2,
    min_value=0.0,
    max_value=1.0,
    step=0.1,
    key="number-input-threshold",
)
st.write("Threshold:", threshold)

offset = ui.number_input("Offset", value=-2, key="number-input-offset", width=280)
st.write("Offset:", offset)
ui.number_input("Locked amount", value=4, disabled=True, key="number-input-disabled", width=280)

st.subheader("Nested controls")
with ui.elements(key="number-input-settings") as el:
    with el.card(key="batch"):
        with el.card_header():
            el.heading("Batch settings")
            el.text("The same numeric input inside a composed card.", variant="muted")
        with el.card_content():
            batch_size = el.number_input(
                "Batch size", value=16, min_value=1, max_value=128, key="batch-size"
            )
st.write("Batch size:", batch_size.value)

st.button("Rerun examples", help="Verify that committed values survive another rerun.")
st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/number_input.md").read_text()
)
