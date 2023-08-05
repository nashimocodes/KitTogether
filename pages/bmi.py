from dateutil.parser import parse
from taipy.gui import notify
from datetime import date

from lib.database.init import get_collection

BMI_PAGE = """
### Your weight info needs to be entered.

<|{weight}|number|label=weight(kg)|>
<|{height}|number|label=height(cm)|>
<|{date_input}|date|hover_text=Date|>
<|{submit}|button|label=submit|on_action=bodyMassIndex|>
<|{result}|text|>

# <|{bmi_data}|chart|x=date|y=bmi|>
"""


def get_bmi_data():
    collection = get_collection("bmi")
    data = list(collection.find({}))
    for item in data:
        item.pop("_id")
        item["date"] = parse(item["date"])

    return data


date_input = date.today()
weight = 0
height = 0
result = 0
bmi_data = get_bmi_data()
print(bmi_data)


def bodyMassIndex(state):
    if state.weight <= 0 or state.height <= 0:
        return
    result = state.weight / (state.height / 100) ** 2
    state.assign("result", result)
    db(state, state.date_input, state.weight, state.height, result)


def db(state, date_input: date, weight: int, height: int, bmi: int):
    collection = get_collection("bmi")
    collection.update_one(
        {"date": date_input.strftime("%d/%m/%Y")},
        {
            "$set": {
                "date": date_input.strftime("%d/%m/%Y"),
                "weight": weight,
                "height": height,
                "bmi": bmi,
            }
        },
        upsert=True,
    )

    notify(state, "success", f"Saved BMI for {date_input}!")
