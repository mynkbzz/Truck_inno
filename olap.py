from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Color

class DemoApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        # Create a big rectangle shape in the center of the window
        with layout.canvas:
            Color(1, 1, 0, 1)  # Set the fill color (blue in this example)
            big_rectangle = Rectangle(pos=(100, 100), size=(800, 600))  # Position and size of the big rectangle

        # Create a smaller rectangle inside the big rectangle
        with layout.canvas:
            Color(1, 0, 0, 1)  # Set the fill color (red in this example)
            small_rectangle = Rectangle(pos=(100, 500), size=(300, 200))  # Position and size of the small rectangle

        return layout

if __name__ == '__main__':
    DemoApp().run()
