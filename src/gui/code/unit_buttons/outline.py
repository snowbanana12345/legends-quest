import pygame
from src.gui.code.unit_buttons.renderable import Renderable


class Outline(Renderable):
    def __init__(self, xlength, ylength, width, color):
        super().__init__(xlength, ylength)
        self.width = width
        self.color = color

    def render(self, screen, xpos, ypos):
        rectangle = pygame.Rect(xpos, ypos, self.xlength, self.ylength)
        pygame.draw.rect(screen, self.color, rectangle, width = self.width)