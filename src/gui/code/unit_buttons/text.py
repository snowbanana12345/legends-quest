import pygame


class Text:
    def __init__(self, text, font_size = 15, color = (255, 255, 255), style = "comicsansms"):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.style = style

    def create_text_obj(self):
        font = pygame.font.SysFont(self.style, self.font_size)
        textobj = font.render(self.text, True, self.color)
        return textobj

    def render(self, surface):
        textobj = self.create_text_obj()
        surface.blit(textobj, (0, 0))

