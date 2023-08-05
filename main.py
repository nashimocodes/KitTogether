from taipy.gui import Gui

from pages.chart import weightInfo


weight = 0
height = 0
result = 0


def bodyMassIndex(state):
    result = state.weight / (state.height / 100) ** 2
    state.assign("result", result)


pages = {
    "chart": weightInfo,
}

if __name__ == "__main__":
    Gui(pages=pages).run(
        use_reloader=True,
    )
