import pygame

from src.gui.code.unit_buttons.square_box import SquareBox

"""
assume the picture frame side length is always 10% of the size of the entire xlength and ylength
the actual picture it occupies is 80% of the length
"""
class PictureFrameWithIcon(SquareBox):
    def __init__(self, xpos, ypos, xlength, ylength, image, frame_image):
        super().__init__(xpos, ypos, xlength, ylength)
        self.image = image
        self.image = pygame.transform.smoothscale(self.image, (int(0.8 * xlength), int(0.8 * ylength)))
        self.frame_image = frame_image
        self.frame_image = pygame.transform.smoothscale(self.frame_image, (xlength, ylength))

    def render(self, screen):
        screen.blit(self.frame_image, (self.xpos, self.ypos))
        screen.blit(self.image, (self.xpos + 0.1 * self.xlength, self.ypos + 0.1 * self.ylength))



