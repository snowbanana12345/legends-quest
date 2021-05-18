import pygame

"""
assume the picture frame side length is always 10% of the size of the entire xlength and ylength
the actual picture it occupies is 80% of the length
"""
class ImageWithFrame:
    def __init__(self, xlength, ylength, image, frame_image):
        self.xlength = xlength
        self.ylength = ylength
        self.image = pygame.transform.smoothscale(image, (int(0.8 * xlength), int(0.8 * ylength)))
        self.frame_image = pygame.transform.smoothscale(frame_image, (int(xlength), int(ylength)))

    def render(self, screen, xpos, ypos):
        screen.blit(self.frame_image, (xpos, ypos))
        screen.blit(self.image, (xpos + 0.1 * self.xlength, ypos + 0.1 * self.ylength))
