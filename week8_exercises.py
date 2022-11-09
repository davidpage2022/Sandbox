"""Week 8 exercises - Kivy"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


class HelloWorld(App):
    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('widget.kv')
        return self.root

    def handle_button_press(self, button):
        print(f"ouch! ('{button.text}')")


HelloWorld().run()
