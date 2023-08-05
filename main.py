from taipy.gui import Gui

from pages.chart import CHART_PAGE

pages = {
    "chart": CHART_PAGE,
}

if __name__ == "__main__":
    Gui(pages=pages).run(
        use_reloader=True,
    )
