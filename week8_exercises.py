"""Week 8 exercises - Kivy"""

from kivy.app import App
from kivy.uix.widget import Widget


class HelloWorld(App):
    def build(self):
        self.root = Widget()
        return self.root


HelloWorld().run()
