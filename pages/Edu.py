from taipy.gui import Gui

DataVisual= """
### Crime Rates against Transgenders
<|{dataset}|chart|mode=lines|x=Year|y[1]=Anti-Transgender|y[2]=Anti-Female|y[3]=Anti-Gender Identity|color[1]=blue|color[2]=green|color[3]=red|Label=Crime Rates against Transgenders|>
"""  # noqa: E501

def get_data(path: str):
    import pandas as pd
    dataset = pd.read_csv(path)
    dataset["Year"]=pd.to_datetime(dataset["Year"], format="%Y")
    return dataset

dataset = get_data("dataset/New_York_Hate_Crimes_2010-2019.csv")