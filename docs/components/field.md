# Field

Field supplies accessible labels, descriptions, validation errors, groups,
legends, and separators around supported Elements controls.

```python
import streamlit as st
import streamlit_shadcn_ui as ui

with ui.elements(key="profile-fields") as el:
    with el.field_set("Profile", description="Public account details."):
        with el.field_group():
            with el.field(
                "Website",
                description="Use a public URL.",
                error="Example validation message.",
            ):
                website = el.input_group(
                    "Website",
                    "example.com",
                    key="website",
                    prefix="https://",
                )
            el.field_separator("Preferences")
            with el.field("Security alerts", orientation="horizontal"):
                alerts = el.checkbox(
                    "Security alerts",
                    key="alerts",
                    value=True,
                )

st.write(website.value, alerts.value)
```

Each Field must contain exactly one `input`, `input_group`, `textarea`,
`select`, `combobox`, `checkbox`, or `switch`. Pass the same semantic label to
the control; the outer Field owns the rendered label and its ARIA connections.
`orientation` accepts `"vertical"`, `"horizontal"`, or `"responsive"`.
Field Set and Field Group accept Fields, nested groups, and separators only.
Native `st.*` children are not supported.
