import pandas as pd
from taipy.gui import Markdown, State, notify

DIABETES_PAGE = Markdown(
    """
# Diabetes
<br />

<|button|label=Load Data|on_action=load_diabetes_dataset|>
<br />
<br />
<|{diabetes_dataset}|chart|type=bar|x=BMI|y=outcome|>
"""
)

diabetes_dataset = pd.DataFrame(columns=["BMI", "outcome"])


def load_diabetes_dataset(state: State):
    notify(state, "info", "Loading data...")
    local_dataset = pd.read_csv("./dataset/diabetes.csv")
    state.assign("diabetes_dataset", local_dataset)
    notify(state, "success", "Data loaded!")
