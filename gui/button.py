class Button:
    def __init__(self, xpos, ypos, xlength, ylength):
        self.pressed = False
        self.xpos = xpos
        self.ypos = ypos
        self.xlength = xlength
        self.ylength = ylength


    def press(self):
        self.pressed = True

    def lift(self):
        self.pressed = False

    def check_inside(self, x, y):
        return (self.xpos <= x <= self.xpos + self.xlength) and (self.ypos <= y <= self.ypos + self.ylength)
