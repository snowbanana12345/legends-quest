from src.gui.button import Button
from src.gui.text_box import TextBox


class TextBoxButton:
    def __init__(self, xpos, ypos, xlength, ylength, text, font_size):
        self.button = Button(xpos, ypos, xlength, ylength)
        self.text_box = TextBox(xpos, ypos, xlength, ylength, text, font_size)

    def render(self, screen):
        self.text_box.render(screen)

    def press(self):
        self.button.press()

    def lift(self):
        self.button.lift()

    def is_pressed(self):
        self.button.is_pressed()

    