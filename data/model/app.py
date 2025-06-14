from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from menuInicial import MenuInicial
from cadastro import Cadastro


class StopwatchApp(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self)-> ComposeResult:
        self.push_screen(Cadastro())

    


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()