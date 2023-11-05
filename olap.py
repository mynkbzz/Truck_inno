from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Color

class DemoApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        # Ask the user for the number of cells (smaller rectangles)
        num_cells = int(input("Enter the number of cells:"))

        # Calculate the size of each smaller rectangle and the gap between them
        big_rectangle_width = 800
        big_rectangle_height = 600
        gap_size = 10  # Adjust this value to control the separation between smaller rectangles
        cell_width = (big_rectangle_width - (num_cells - 1) * gap_size) / num_cells
        cell_height = (big_rectangle_height - (num_cells - 1) * gap_size) / num_cells

        with layout.canvas:
            Color(1, 1, 0, 1)  # Set the fill color (blue in this example)
            big_rectangle = Rectangle(pos=(100, 100), size=(big_rectangle_width, big_rectangle_height))

        for i in range(num_cells):
            for j in range(num_cells):
                with layout.canvas:
                    Color(1, 0, 0, 1)  # Set the fill color (red in this example)
                    x = 100 + i * (cell_width + gap_size)
                    y = 100 + j * (cell_height + gap_size)
                    small_rectangle = Rectangle(pos=(x, y), size=(cell_width, cell_height))

        return layout

if __name__ == '__main__':
    DemoApp().run()
