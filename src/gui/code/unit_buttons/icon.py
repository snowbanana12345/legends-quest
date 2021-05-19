import pygame

from src.gui.code.unit_buttons.renderable import Renderable



class Icon(Renderable):
    def __init__(self, xlength, ylength, image):
        super().__init__(xlength, ylength)
        self.image = image
        self.scale()

    def scale(self):
        self.image = pygame.transform.smoothscale(self.image, (self.xlength, self.ylength))

    def render(self, screen, xpos, ypos):
        screen.blit(self.image, (xpos, ypos))