# Combobox

Combobox combines text search with a single or multiple selection. Filtering
happens in the browser, so typing does not rerun Python. Selecting, removing,
or clearing a value commits state and reruns Python once.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

release = ui.combobox(
    "Release channel",
    ["Stable", "Beta", "Canary"],
    value="Stable",
    key="release-channel",
    placeholder="Search channels",
)
topics = ui.combobox(
    "Topics",
    ["Components", "Elements", "Theming"],
    value=["Components"],
    key="topics",
    selection_mode="multiple",
)
st.write(release, topics)
```

`selection_mode` is `"single"` by default and returns one original Python
option or `None`. `"multiple"` returns a list of original Python options in
selection order. Options must be unique; use `format_func` or `ui.Choice` to
separate display labels from returned values. `empty_message`, `clearable`,
`disabled`, `on_change`, and the normal width options are supported.

The same control is available as `el.combobox(...)` inside Elements. Its
stateful node requires a key and returns an `ElementHandle`.
