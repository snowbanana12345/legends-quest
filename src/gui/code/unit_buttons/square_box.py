import pygame


class SquareBox:
    def __init__(self, xpos, ypos, xlength, ylength, outline_width = 3, outline = False):
        self.xpos = xpos
        self.ypos = ypos
        self.xlength = xlength
        self.ylength = ylength
        self.outline = outline
        self.outline_width = 3
        self.outline_color = (255, 255, 255)

    def enable_outline(self):
        self.outline = True

    def disable_outline(self):
        self.outline = False

    def set_outline_width(self, width):
        self.outline_width = width

    def set_outline_color(self, color):
        self.outline_color = color

    def render(self, surface):
        pygame.draw.rect(surface, self.outline_color, (self.xpos, self.ypos, self.xlength, self.ylength), self.outline_width)