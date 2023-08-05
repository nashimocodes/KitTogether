BMI_PAGE = """

### Your weight info needs to be entered.

<|{weight}|number|label=weight(kg)|on_change=bodyMassIndex|>
<|{height}|number|label=height(cm)|on_change=bodyMassIndex|>
# <|{date}|date|label=date|>
<|{submit}|button|label=submit|on_change=bodyMassIndex|>
<|{result}|text|label=BMI|>
"""
