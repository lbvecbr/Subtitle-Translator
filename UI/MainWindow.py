from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    app = MainApp()
    app.run()