import pygame


class Text:
    def __init__(self, text, font_size = 15, color = (255, 255, 255), style = "comicsansms"):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.style = style
        self.font = pygame.font.SysFont(self.style, self.font_size)
        self.text_obj = self.font.render(self.text, True, self.color)

    def render(self, surface):
        surface.blit(self.text_obj, (0, 0))

