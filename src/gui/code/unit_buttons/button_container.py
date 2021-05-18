from src.gui.code.unit_buttons.button import Button


class ButtonContainer:
    def __init__(self, xpos, ypos, xlength, ylength):
        self.button = Button(xpos, ypos, xlength, ylength)

    def press(self):
        self.button.press()

    def lift(self):
        self.button.lift()

    def is_pressed(self):
        self.button.is_pressed()