import pygame


class SquareBox:
    def __init__(self, xpos, ypos, xlength, ylength):
        self.xpos = xpos
        self.ypos = ypos
        self.xlength = xlength
        self.ylength = ylength

    def render(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.xpos, self.ypos, self.xlength, self.ylength), 3)