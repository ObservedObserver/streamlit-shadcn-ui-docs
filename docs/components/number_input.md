## Number input with controls

Available in **1.2.0**. Enter a number directly or use the decrement and
increment buttons. The buttons have 44 px touch targets and use the same
shadcn Input and Button sources as the rest of the library.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

quantity = ui.number_input(
    "Quantity",
    value=1,
    min_value=1,
    max_value=10,
    step=1,
    key="quantity",
)
st.write("Quantity:", quantity)
```

Use a float argument to enable fractional values:

```python
import streamlit as st
import streamlit_shadcn_ui as ui

threshold = ui.number_input(
    "Threshold",
    value=0.2,
    min_value=0.0,
    max_value=1.0,
    step=0.1,
    key="threshold",
)
st.write("Threshold:", threshold)
```

| Parameter | Default | Behavior |
| --- | --- | --- |
| `label` | Required | Visible, accessible label |
| `value` | `0` | Initial numeric value; a changed Python default resets the field |
| `min_value`, `max_value` | `None` | Optional inclusive bounds; equal bounds are allowed |
| `step` | `None` | Defaults to `1` in integer mode and `0.01` in float mode |
| `key` | `None` | Stable identity for dynamic or repeated controls |
| `disabled` | `False` | Disables typing and both buttons |
| `on_change` | `None` | No-argument callback after a committed value change |
| `width` | `"stretch"` | `"content"`, `"stretch"`, or an integer pixel width |

The return type is `int` when every supplied numeric argument is an integer.
If any value, bound, or step is a float, the result is a `float`. Booleans,
NaN, infinity, nonpositive steps, and numbers outside
`[-9007199254740991, 9007199254740991]` are rejected. `value=None`, Decimal,
currency formatting, and locale-specific number text are not supported.

Typing stays local until Enter or blur. Empty or invalid drafts restore the
last committed value, including fractional text in integer mode. Valid
out-of-range text is clamped when committed. Escape discards an uncommitted
draft. Arrow Up/Down step the value; Home/End select a configured minimum or
maximum. Wheel scrolling does not change the value. Step buttons adjust the
current value without snapping it to a separate step grid.

Read the current number from the return value. As with other components in
this library, `st.session_state[key]` is not a public numeric state binding.

## Inside an Elements tree

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="batch-settings") as el:
    with el.card(key="settings"):
        with el.card_header():
            el.heading("Batch settings")
        with el.card_content():
            batch_size = el.number_input(
                "Batch size", value=16, min_value=1, max_value=128, key="batch-size"
            )

st.write("Batch size:", batch_size.value)
```

`el.number_input` requires a node `key`, returns `ElementHandle[int | float]`,
and accepts an Elements callback with its typed `ElementEvent`. It shares
the standalone component's numeric validation and interaction behavior;
layout width comes from the surrounding Elements tree.
