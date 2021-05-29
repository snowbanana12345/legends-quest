from src.gui.code.unit_buttons.box import Box
from src.gui.code.unit_buttons.button import Button


class ButtonContainer(Box):
    def __init__(self, xpos, ypos, xlength, ylength):
        super().__init__(xpos, ypos, xlength, ylength)
        self.button = Button(xpos, ypos, xlength, ylength)

    def press(self):
        self.button.press()

    def lift(self):
        self.button.lift()

    def is_pressed(self):
        return self.button.is_pressed()

    def flip(self):
        self.button.flip()