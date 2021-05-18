from src.gui.code.unit_buttons.button_container import ButtonContainer
from src.gui.code.unit_buttons.icon import Icon


class IconButton(ButtonContainer):
    def __init__(self, xpos, ypos, xlength, ylength, image):
        super().__init__(xpos, ypos, xlength, ylength)
        self.icon = Icon(xpos, ypos, xlength, ylength, image)

    def render(self, screen):
        self.icon.render(screen)

