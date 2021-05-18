from src.gui.code.unit_buttons.button_container import ButtonContainer
from src.gui.code.unit_buttons.picture_frame import PictureFrameWithIcon


class PictureFrameButton(ButtonContainer):
    def __init__(self, xpos, ypos, xlength, ylength, image, frame_image):
        super().__init__(xpos, ypos, xlength, ylength)
        self.picture_frame = PictureFrameWithIcon(xpos, ypos, xlength, ylength, image, frame_image)

    def render(self, screen):
        self.picture_frame.render(screen)

