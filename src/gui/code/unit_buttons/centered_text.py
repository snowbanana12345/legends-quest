from src.gui.code.unit_buttons.text import Text


class CenteredText(Text):
    def __init__(self, text, font_size = 15, color = (255, 255, 255), style = "comicsansms"):
        super().__init__(text, font_size, color, style)

    def render(self, surface):
        textobj = self.create_text_obj()
        xpos = surface.get_width() / 2 - textobj.get_width()/2
        ypos = surface.get_height() / 2 - textobj.get_height()/2
        surface.blit(textobj, (xpos, ypos))