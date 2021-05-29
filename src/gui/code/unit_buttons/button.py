from src.gui.code.unit_buttons.box import Box


class Button(Box):
    def __init__(self, xpos, ypos, xlength, ylength):
        super().__init__(xpos, ypos, xlength, ylength)
        self.pressed = False

    def press(self):
        self.pressed = True

    def lift(self):
        self.pressed = False

    def is_pressed(self):
        return self.pressed

    def flip(self):
        if self.pressed:
            self.pressed = False
        else:
            self.pressed = True
