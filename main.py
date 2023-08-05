from taipy.gui import Gui, notify, navigate, Html
from dotenv import load_dotenv

from pages.bmi import BMI_PAGE, bodyMassIndex, weight, height, result  # noqa: F401
from pages.home_page import HOME_PAGE
from lib.database.init import client

load_dotenv()

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "Landing": Html("./static/home.html"),
    "Home": HOME_PAGE,
    "BMI": BMI_PAGE,
    "About": "About",
}
page_names = [page for page in pages.keys() if page != "/"]


def menu_action(state, id, action, payload):
    page = payload["args"][0]
    navigate(state, page)


def dot_it(state):
    print("I'm a dot!")
    notify(state, "warning", "I'm a dot!")


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
