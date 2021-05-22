import pygame

from src.gui.code.unit_buttons.centered_text import CenteredText
from src.gui.code.unit_buttons.renderable import Renderable

"""
Renders a text with a background
xlength, ylength are the width and height of the box
text is a string

"""
class TextBox(Renderable):
    def __init__(self, xlength, ylength, background, text):
        super().__init__(xlength, ylength)
        self.background = background
        self.text = CenteredText(text)

    def scale(self):
        self.background = pygame.transform.smoothscale(self.background, (self.xlength, self.ylength))

    def render(self, screen, xpos, ypos):
        self.text.render(self.background)
        screen.blit(self.background, (xpos, ypos))


