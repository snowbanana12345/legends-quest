from src.gui.code.unit_buttons.text_box import TextBox
from src.gui.code.unit_buttons.text_box_button import TextBoxButton


class SelectableTextBoxButton(TextBoxButton):
    def __init__(self, xpos, ypos, xlength, ylength, background_unselect, background_select, text):
        super().__init__(xpos, ypos, xlength, ylength, background_unselect, text)
        self.select_text_box = TextBox(xlength, ylength, background_select, text)

    def render(self, screen):
        if not self.is_pressed():
            self.text_box.render(screen, self.xpos, self.ypos)
        else:
            self.select_text_box.render(screen, self.xpos, self.ypos)
