from taipy.gui import Gui, notify, navigate, Html
from dotenv import load_dotenv

from pages.bmi import *
from pages.home_page import HOME_PAGE
from lib.database.init import client  # keep

from pages.Edu import *

load_dotenv()

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "Landing": Html("./static/home.html"),
    "Home": HOME_PAGE,
    "BMI": BMI_PAGE,  # noqa: F405
    "About": "About",
    "DataVisual": DataVisual,
}
page_names = [page for page in pages.keys() if page != "/"]


def menu_action(state, _id, _action, payload):
    page = payload["args"][0]
    navigate(state, page)


if __name__ == "__main__":
    gui = Gui(
        css_file="./style.css",
        env_filename=".env",
    )

    gui.add_pages(pages)

    gui.run(
        use_reloader=True,
        title="GG",
    )
