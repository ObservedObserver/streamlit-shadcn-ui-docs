from pathlib import Path

import streamlit as st
import streamlit_shadcn_ui as ui


st.header("Field")
st.caption("Field supplies labels, descriptions, errors, groups, and separators.")

with ui.elements(key="field-demo") as el:
    with el.field_set(
        "Profile",
        description="Details shown on your public profile.",
    ):
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
                    start_icon="link",
                    clearable=True,
                )
            el.field_separator("Preferences")
            with el.field(
                "Release channel",
                description="Search before selecting.",
            ):
                release = el.combobox(
                    "Release channel",
                    ["Stable", "Beta", "Canary"],
                    key="release",
                    value="Stable",
                )
            with el.field(
                "Security alerts",
                description="Receive important account notices.",
                orientation="horizontal",
            ):
                alerts = el.checkbox(
                    "Security alerts",
                    key="security-alerts",
                    value=True,
                )

st.write(
    {
        "website": website.value,
        "release": release.value,
        "security_alerts": alerts.value,
    }
)

st.markdown(
    (Path(__file__).resolve().parents[1] / "docs/components/field.md").read_text()
)
