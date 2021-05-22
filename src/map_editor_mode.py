import os
import pygame
import definitions
from src.gui.code.composite.scrollable_array import ScrollableFrameIconButtonArray
from src.gui.code.unit_buttons.icon import Icon
from src.gui.code.unit_buttons.selectable_text_box_button import SelectableTextBoxButton
from src.map.camera import Camera
from src.map.map_editor.map_editor import MapEditor
from src.map.map_editor.map_save_load import MapSaveLoad
from src.map.texture_id_manager import TextureIdManager

root_dir = definitions.ROOTDIR
pygame.init()

# ----- variables ------

title = "Map Editor Mode"
screen_width = 1000
screen_height = 800
frame_rate = 30

camera_x_center = 0
camera_y_center = 0
world_grid_x_length = 20
world_grid_y_length = 20
camera_velocity = 10

TEXTURE_MODE = "TEXTURE_MODE"
TILE_TYPE_MODE = "TILE_TYPE_MODE"
mode = "TEXTURE_MODE"

texture_category = "forest"
curr_texture = None
curr_texture_icon_x, curr_texture_icon_y = 800, 200
scrollable_x_pos, scrollable_y_pos = 700, 400
scrollable_x_length, scrollable_y_length = 300, 400

TILE_TYPE_VALID = "VALID"
TILE_TYPE_INVALID = "INVALID"
curr_tile_type = "VALID"

grid_x = 100
grid_y = 100
grid_line_width = 2
pickle_file_path = os.path.join(root_dir, "data\\game_data\\maps","tutorial_island_forest.pickle")

# ----- initialize classes -----
texture_id_manager = TextureIdManager()
map_save_load = MapSaveLoad.pickle_load(pickle_file_path)
camera = Camera(screen_width, screen_height, camera_x_center, camera_y_center
                , world_grid_x_length, world_grid_y_length, texture_id_manager)
camera.set_grid_line_width(grid_line_width)
map_editor = MapEditor()
clock = pygame.time.Clock()


# ----- load data ------
if map_save_load:
    texture_data = map_save_load.get_grid_texture_id_map()
    tile_type_data = map_save_load.get_grid_tile_type_map()
    map_editor.set_grid_texture_id_map(texture_data)
    map_editor.set_tile_type_map(tile_type_data)
    camera.set_grid_texture_map(texture_data)
    camera.set_tile_type_map(tile_type_data)
else :
    map_save_load = MapSaveLoad()
    map_editor.create_empty_maps(grid_x, grid_y)
    camera.set_grid_texture_map(map_editor.get_grid_texture_map())
    camera.set_tile_type_map(map_editor.get_grid_tile_type_map())

# ---------- gui components ------------
texture_selection_scroller = ScrollableFrameIconButtonArray(scrollable_x_pos, scrollable_y_pos
                                                            , scrollable_x_length, scrollable_y_length, 3, 4)
image_x_length, image_y_length = texture_selection_scroller.get_required_image_dimensions()
forest_tiles = texture_id_manager.get_category(texture_category)
active_texture_icons = {}
for key in forest_tiles:
    button_icon = Icon(image_x_length, image_y_length, forest_tiles[key])
    active_texture_icons[key] = button_icon
    texture_selection_scroller.add_button(button_icon, key)
obama = pygame.image.load(os.path.join(definitions.ROOTDIR, "src\\gui\\images\\test_images", "barrack_obama.png"))
obama_icon = Icon(image_x_length, image_y_length, obama)
texture_selection_scroller.set_default_image(obama_icon)

enchanted_wood_button_background = pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\gui_backgrounds", "enchanted_wood_100_x_50.png"))
select_enchanted_wood_button_background =  pygame.image.load(os.path.join(root_dir, "src\\gui\\images\\gui_backgrounds", "selected_enchanted_wood_100_x_50.png"))

texture_mode_button = SelectableTextBoxButton(700, 50, 100, 50, enchanted_wood_button_background.copy()
                                          , select_enchanted_wood_button_background.copy(), "TEXTURE")
tile_type_mode_button = SelectableTextBoxButton(700, 100, 100, 50, enchanted_wood_button_background.copy()
                                          , select_enchanted_wood_button_background.copy(), "TILE TYPE")
valid_tile_type_button = SelectableTextBoxButton(800, 50, 100, 50, enchanted_wood_button_background.copy()
                                          , select_enchanted_wood_button_background.copy(), "VALID")
invalid_tile_type_button = SelectableTextBoxButton(800, 100, 100, 50, enchanted_wood_button_background.copy()
                                          , select_enchanted_wood_button_background.copy(), "INVALID")

texture_mode_button.flip()
valid_tile_type_button.flip()

# ---- pygame main loop -----

pygame.display.set_caption(title)
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    screen.fill((0, 0, 0))

    if mode == TEXTURE_MODE:
        camera.disable_tile_type_viewing()
    if mode == TILE_TYPE_MODE:
        camera.enable_tile_type_viewing()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_y_center -= camera_velocity
    if keys[pygame.K_s]:
        camera_y_center += camera_velocity
    if keys[pygame.K_a]:
        camera_x_center -= camera_velocity
    if keys[pygame.K_d]:
        camera_x_center += camera_velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if texture_mode_button.check_inside(mouse_x, mouse_y):
                mode = TEXTURE_MODE
                if not texture_mode_button.is_pressed():
                    texture_mode_button.flip()
                    tile_type_mode_button.flip()
            elif tile_type_mode_button.check_inside(mouse_x, mouse_y):
                mode = TILE_TYPE_MODE
                if not tile_type_mode_button.is_pressed():
                    texture_mode_button.flip()
                    tile_type_mode_button.flip()
            elif valid_tile_type_button.check_inside(mouse_x, mouse_y):
                curr_tile_type = TILE_TYPE_VALID
                if not valid_tile_type_button.is_pressed():
                    valid_tile_type_button.flip()
                    invalid_tile_type_button.flip()
            elif invalid_tile_type_button.check_inside(mouse_x, mouse_y):
                curr_tile_type = TILE_TYPE_INVALID
                if not invalid_tile_type_button.is_pressed():
                    valid_tile_type_button.flip()
                    invalid_tile_type_button.flip()

            elif texture_selection_scroller.check_inside(mouse_x, mouse_y):
                curr_texture = texture_selection_scroller.click(mouse_x, mouse_y)

            # from this point on, the mouse should either land on a grid tile, or outside the grid tile
            # all the gui components have already been checked
            elif mode == TEXTURE_MODE:
                if curr_texture is not None:
                    curr_grid_pos = camera.click_tile(mouse_x, mouse_y)
                    if curr_grid_pos:
                        stored_key = texture_id_manager.catenate_category_key(texture_category, curr_texture)
                        camera.update_texture(curr_grid_pos, stored_key)
                        map_editor.update_tile_texture_id(curr_grid_pos[0], curr_grid_pos[1], stored_key)
            elif mode == TILE_TYPE_MODE:
                curr_grid_pos = camera.click_tile(mouse_x, mouse_y)
                if curr_grid_pos is not None:
                    map_editor.update_tile_type(curr_grid_pos[0], curr_grid_pos[1], curr_tile_type)

    camera.set_center(camera_x_center, camera_y_center)
    camera.render(screen)

    if curr_texture:
        active_texture_icons[curr_texture].render(screen, curr_texture_icon_x, curr_texture_icon_y)
    else:
        obama_icon.render(screen, curr_texture_icon_x, curr_texture_icon_y)

    texture_selection_scroller.render(screen)
    texture_mode_button.render(screen)
    tile_type_mode_button.render(screen)
    valid_tile_type_button.render(screen)
    invalid_tile_type_button.render(screen)

    pygame.display.update()
    clock.tick(frame_rate)

map_save_load.set_grid_texture_id_map(map_editor.get_grid_texture_map())
map_save_load.set_grid_tile_type_map(map_editor.get_grid_tile_type_map())
map_save_load.pickle_save(pickle_file_path)