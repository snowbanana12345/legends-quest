import pygame
import definitions
import os

from src.gui.code.unit_buttons.picture_frame import PictureFrameWithIcon

title = "gui test"
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((1000, 800))
running = True

root_dir = definitions.ROOTDIR

waifu_1 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_1.png"))
waifu_2 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_2.png"))
tsudere_1 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "tsudere_1.png"))
tsudere_2 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "tsudere_2.png"))
dark_souls_knight = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "dark_souls_knight.png"))
obama = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "barrack_obama.png"))

vines_frame = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "veins_frame.png"))
picture_frame = PictureFrameWithIcon(350, 250, 400, 400, waifu_1, vines_frame)

while running:
    picture_frame.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()