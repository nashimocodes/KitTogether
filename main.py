from taipy.gui import Gui, notify, navigate

from pages.home_page import HOME_PAGE

pages = {
    "/": "<|menu|lov={page_names}|on_action=menu_action|>",
    "Home": HOME_PAGE,
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
    Gui(
        pages=pages,
        css_file="./style.css",
    ).run(
        use_reloader=True,
        title="GG",
    )
