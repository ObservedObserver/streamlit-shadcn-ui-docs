This is a component for testing and experimenting with new features.

It allows you to use any component like using in a React Framework.

What you can benefit it from:
+ You can build nested components, all `streamlit-shadhcn-ui` component can combine together.
+ It allows you to write html and tailwindcss directly in python, without any extra work.

**This component is still in experimental stage, it may change in the future.** Now I only refactor several components to work in this mode. If you have any idea or suggestion, please open an issue.

### Basic Usage

Using `with` statement to create a component
```python
with ui.card(key="base_ele_card_l1"):
    with ui.card(key="base_ele_card_l2"):
        ui.element("input", key="nst2_input", label="Value")
        ui.element("button", key="nst2_btn", text="Nest Submmit", variant="outline")

    ui.element("button", key="nst_btn", text="Hello World")
```

Using without `with` statement, remember to call `render` method to render the component.
```python
st.header("Nest Element 2")
card = ui.element("card", key="base_ele_2")
card2 = ui.element("card", key="base_ele2_2")
card2.add_child(ui.element("input", key="nst2_input_2", label="Value"))
card2.add_child(ui.element("button", key="nst2_btn_2", text="Nest Submmit", variant="outline"))
card.add_child(card2)
card.add_child(ui.element("button", key="nst_btn_2", text="Hello World"))
card.render()
```