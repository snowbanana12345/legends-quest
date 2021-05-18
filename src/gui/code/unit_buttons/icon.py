import pygame
from src.gui.code.unit_buttons.square_box import SquareBox


class Icon(SquareBox):
    def __init__(self, xpos, ypos, xlength, ylength, image):
        super().__init__(xpos, ypos, xlength, ylength)
        self.image = image
        self.image = pygame.transform.smoothscale(self.image, (xlength, ylength))

    def render(self, screen):
        super().render(screen)
        screen.blit(self.image, (self.xpos, self.ypos))