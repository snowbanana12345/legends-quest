from src.gui.code.unit_buttons.text import Text


class CenteredText(Text):
    def __init__(self, text, font_size = 15, color = (255, 255, 255), style = "comicsansms"):
        super().__init__(text, font_size, color, style)

    def render(self, surface):
        xpos = surface.get_width() / 2 - self.text_obj.get_width()/2
        ypos = surface.get_height() / 2 - self.text_obj.get_height()/2
        surface.blit(self.text_obj, (xpos, ypos))