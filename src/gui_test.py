import pygame
import definitions
import os

from src.gui.code.composite.scrollable_array import ScrollableFrameIconButtonArray
from src.gui.code.unit_buttons.icon_button import IconButton
from src.gui.code.unit_buttons.image_with_frame import ImageWithFrame
from src.gui.code.unit_buttons.outline import Outline
from src.gui.code.unit_buttons.selectable_text_box_button import SelectableTextBoxButton
from src.gui.code.unit_buttons.text_box import TextBox

title = "gui test"
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((1000, 800))
running = True

root_dir = definitions.ROOTDIR

# ---------- load images -----------------
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
enchanted_wood_button_background = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\gui_backgrounds", "enchanted_wood_100_x_50.png"))
select_enchanted_wood_button_background =  pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\gui_backgrounds", "selected_enchanted_wood_100_x_50.png"))

# --------- create gui components ---------------------
scrollable_array_test = ScrollableFrameIconButtonArray(350, 250, 400, 400, 3, 2)
width, height = scrollable_array_test.get_required_image_dimensions()

waifu_1_frame = ImageWithFrame(width, height,waifu_1, vines_frame)
waifu_2_frame = ImageWithFrame(width, height,waifu_2, vines_frame)
waifu_3_frame = ImageWithFrame(width, height,waifu_3, vines_frame)
waifu_4_frame = ImageWithFrame(width, height,waifu_4, vines_frame)
tsudere_1_frame = ImageWithFrame(width, height, tsudere_1, vines_frame)
tsudere_2_frame = ImageWithFrame(width, height, tsudere_2, vines_frame)
dark_souls_frame = ImageWithFrame(width, height, dark_souls_knight, vines_frame)
obama_frame = ImageWithFrame(width, height, obama, vines_frame)
muscular_1_frame = ImageWithFrame(width, height, musclular_1, vines_frame)
muscular_2_frame = ImageWithFrame(width, height, musclular_2, vines_frame)
muscular_3_frame = ImageWithFrame(width, height, musclular_3, vines_frame)

scrollable_array_test.add_button(waifu_1_frame, "waifu_1")
scrollable_array_test.add_button(waifu_2_frame, "waifu_2")
scrollable_array_test.add_button(tsudere_1_frame, "tsudere_1")
scrollable_array_test.add_button(tsudere_2_frame, "tsudere_2")
scrollable_array_test.add_button(dark_souls_frame, "dark_souls_knight")
scrollable_array_test.add_button(obama_frame, "obama")
scrollable_array_test.add_button(waifu_3_frame, "waifu_3")
scrollable_array_test.add_button(waifu_4_frame, "waifu_4")
scrollable_array_test.add_button(muscular_1_frame, "musclular_1")
scrollable_array_test.add_button(muscular_2_frame, "musclular_2")
scrollable_array_test.add_button(muscular_3_frame, "musclular_3")

up_arrow_button = IconButton(300, 250, 50, 200, arrow_up)
down_arrow_button = IconButton(300, 450, 50, 200, arrow_down)
outline = Outline(470, 420, 10, (255, 255, 255))

text_box_1 = TextBox(100, 50, enchanted_wood_button_background, "BLAH")
text_box_button = SelectableTextBoxButton(100, 200, 100, 50, enchanted_wood_button_background
                                          , select_enchanted_wood_button_background, "BLAHBLAH")

# ------------ main loop --------------------
while running:
    screen.fill((0,0,0))
    recieved_button_id = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if scrollable_array_test.check_inside(mouse_x, mouse_y):
                recieved_button_id = scrollable_array_test.click(mouse_x, mouse_y)
            elif up_arrow_button.check_inside(mouse_x, mouse_y):
                scrollable_array_test.move_pointer_up()
            elif down_arrow_button.check_inside(mouse_x, mouse_y):
                scrollable_array_test.move_pointer_down()
            elif text_box_button.check_inside(mouse_x, mouse_y):
                text_box_button.flip()



    if recieved_button_id:
        print(recieved_button_id)

    text_box_button.render(screen)
    #text_box_1.render(screen, 100, 100)
    outline.render(screen, 290, 240)
    up_arrow_button.render(screen)
    down_arrow_button.render(screen)
    scrollable_array_test.render(screen)
    pygame.display.update()