class Box:
    def __init__(self, xpos, ypos, xlength, ylength):
        self.xpos = xpos
        self.ypos = ypos
        self.xlength = xlength
        self.ylength = ylength

    def check_inside(self, x, y):
        return (self.xpos <= x <= self.xpos + self.xlength) and (self.ypos <= y <= self.ypos + self.ylength)