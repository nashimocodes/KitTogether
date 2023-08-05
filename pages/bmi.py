from taipy.gui import Gui

# <|{date}|date|hover_text=Date|>
BMI_PAGE = """

### Your weight info needs to be entered.

<|{weight}|number|label=weight(kg)|on_change=bodyMassIndex|>
<|{height}|number|label=height(cm)|on_change=bodyMassIndex|>
<|{submit}|button|label=submit|on_action=bodyMassIndex|>
<|{result}|text|>
"""


weight = 0
height = 0
result = 0


def bodyMassIndex(state):
    result = state.weight / (state.height / 100) ** 2
    state.assign("result", result)


# def setup_partial(gui: Gui):
#     gui.add_partial("BMI_PAGE", BMI_PAGE)
