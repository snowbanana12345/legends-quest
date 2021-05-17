import pygame
from gui.square_box import SquareBox


class TextBox(SquareBox):
    def __init__(self, xpos, ypos, xlength, ylength, text, font_size):
        super().__init__(xpos, ypos, xlength, ylength)
        self.text = text
        self.font_size = font_size
        self.xcenter = xpos + xlength / 2
        self.ycenter = ypos + ylength / 2

    def render(self, surface):
        super().render(surface)
        font = pygame.font.SysFont("comicsansms", self.font_size)
        textobj = font.render(self.text, True, (255, 255, 255))
        text_xpos = self.xcenter - textobj.get_width() / 2
        text_ypos = self.ycenter - textobj.get_height() / 2
        surface.blit(textobj, (text_xpos, text_ypos))
