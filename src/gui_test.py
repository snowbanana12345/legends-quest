import pygame
import definitions
import os

from src.gui.code.composite.scrollable_array import ScrollableFrameIconButtonArray
from src.gui.code.unit_buttons.icon_button import IconButton
from src.gui.code.unit_buttons.picture_frame import PictureFrameWithIcon

title = "gui test"
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((1000, 800))
running = True

root_dir = definitions.ROOTDIR

waifu_1 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_1.png"))
waifu_2 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_2.png"))
waifu_3 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_3.png"))
waifu_4 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "waifu_3.png"))
tsudere_1 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "tsudere_1.png"))
tsudere_2 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "tsudere_2.png"))
dark_souls_knight = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "dark_souls_knight.png"))
obama = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "barrack_obama.png"))
vines_frame = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "veins_frame.png"))
musclular_1 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "muscular_1.png"))
musclular_2 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "muscular_2.png"))
musclular_3 = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "muscular_3.png"))

arrow_up =  pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "enchanted_up_arrow.png"))
arrow_down =  pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\test_images", "enchanted_down_arrow.png"))

scrollable_array_test = ScrollableFrameIconButtonArray(350, 250, 400, 400, 3, 2)
scrollable_array_test.add_button(waifu_1, vines_frame, "waifu_1")
scrollable_array_test.add_button(waifu_2, vines_frame, "waifu_2")
scrollable_array_test.add_button(tsudere_1, vines_frame, "tsudere_1")
scrollable_array_test.add_button(tsudere_2, vines_frame, "tsudere_2")
scrollable_array_test.add_button(dark_souls_knight, vines_frame, "dark_souls_knight")
scrollable_array_test.add_button(obama, vines_frame, "obama")
scrollable_array_test.add_button(waifu_3, vines_frame, "waifu_3")
scrollable_array_test.add_button(waifu_4, vines_frame, "waifu_4")
scrollable_array_test.add_button(musclular_1, vines_frame, "musclular_1")
scrollable_array_test.add_button(musclular_2, vines_frame, "musclular_2")
scrollable_array_test.add_button(musclular_3, vines_frame, "musclular_3")

up_arrow_button = IconButton(300, 250, 50, 200, arrow_up)
down_arrow_button = IconButton(300, 450, 50, 200, arrow_down)


while running:
    recieved_button_id = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if scrollable_array_test.check_inside(mouse_x, mouse_y):
                recieved_button_id = scrollable_array_test.click(mouse_x, mouse_y)
            elif up_arrow_button.check_inside(mouse_x, mouse_y):
                print("clicked up arrow")
                scrollable_array_test.move_pointer_up()
            elif down_arrow_button.check_inside(mouse_x, mouse_y):
                print("clicked down arrow")
                scrollable_array_test.move_pointer_down()

    if recieved_button_id:
        print(recieved_button_id)
    up_arrow_button.render(screen)
    down_arrow_button.render(screen)
    scrollable_array_test.render(screen)
    pygame.display.update()