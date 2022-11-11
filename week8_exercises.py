"""Week 8 exercises - Kivy"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder


class HelloWorld(App):
    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('widget.kv')

        number_of_button_to_add = 3
        for i in range(1, number_of_button_to_add + 1):
            button = Button(text=f"Button #{i}")
            button.bind(on_press=self.handle_button_press)
            self.root.add_widget(button)

        return self.root

    def handle_button_press(self, button):
        # print(self, button, target_id, what)
        button.text = f"ouch! ('{button.text}')"

        # self.root.ids.main_label.text = f"ouch! ('{button.text}')"
        # print(f"ouch! ('{button.text}')")


HelloWorld().run()
