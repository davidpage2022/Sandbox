"""Week 8 exercises - Kivy"""

from kivy.app import App, Widget


class HelloWorld(App):
    def build(self):
        self.root = Widget()
        return self.root


HelloWorld().run()
