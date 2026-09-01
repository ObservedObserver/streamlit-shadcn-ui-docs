# Input Group

Input Group composes an Input with serializable text, icon, clear, and copy
addons. It does not accept arbitrary React or Streamlit children.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

website = ui.input_group(
    "Website",
    "docs.example.com",
    key="website",
    type="url",
    prefix="https://",
    suffix="public",
    start_icon="link",
    clearable=True,
    copyable=True,
    max_length=64,
)
st.write(website)
```

Typing remains local until Enter or blur. Clear commits an empty value and
reruns Python. Copy writes the current draft to the clipboard without a rerun.
Supported start icons are `"at-sign"`, `"dollar-sign"`, `"link"`, `"mail"`,
and `"search"`. Input types are `"text"`, `"email"`, `"password"`,
`"search"`, `"tel"`, and `"url"`.

`el.input_group(...)` provides the same control inside Elements. It requires a
node key and returns an `ElementHandle[str]`.
