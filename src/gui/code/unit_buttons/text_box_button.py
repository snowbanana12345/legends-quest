from src.gui.code.unit_buttons.button_container import ButtonContainer
from src.gui.code.unit_buttons.text_box import TextBox


class TextBoxButton(ButtonContainer):
    def __init__(self, xpos, ypos, xlength, ylength, text, font_size):
        super().__init__(xpos, ypos, xlength, ylength)
        self.text_box = TextBox(xpos, ypos, xlength, ylength, text, font_size)

    def render(self, screen):
        self.text_box.render(screen)


    