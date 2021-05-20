import os
import pygame
import definitions
from src.gui.code.composite.scrollable_array import ScrollableFrameIconButtonArray
from src.gui.code.unit_buttons.icon import Icon
from src.map.camera import Camera
from src.map.map_editor.map_editor import MapEditor
from src.map.map_editor.map_save_load import MapSaveLoad
from src.map.texture_id_manager import TextureIdManager

title = "Map Editor Mode"
screen_width = 1000
screen_height = 800

camera_x_center = 0
camera_y_center = 0
world_grid_x_length = 20
world_grid_y_length = 20
camera_velocity = 10

modes = ["TEXTURE_MODE", "TILE_TYPE_MODE"]
mode = "TEXTURE_MODE"

curr_texture = None
curr_texture_icon_x, curr_texture_icon_y = 800, 200
scrollable_x_pos, scrollable_y_pos = 700, 400
scrollable_x_length, scrollable_y_length = 300, 400

grid_x = 100
grid_y = 100
grid_line_width = 2
file_name = "tutorial_island_forest"

# ----- initialize classes -----
texture_id_manager = TextureIdManager()
map_save_load = MapSaveLoad()
camera = Camera(screen_width, screen_height, camera_x_center, camera_y_center
                , world_grid_x_length, world_grid_y_length, texture_id_manager)
camera.set_grid_line_width(grid_line_width)
map_editor = MapEditor()


# ----- load data ------
loaded = map_save_load.load(file_name)
texture_data = {}
tile_type_data = {}
if loaded: # the file already exists, point everything to this data set
    texture_data = map_save_load.get_grid_texture_id_map()
    tile_type_data = map_save_load.get_grid_tile_type_map()
    map_editor.set_grid_texture_id_map(texture_data)
    map_editor.set_tile_type_map(tile_type_data)
else : # we started off with an empty file, we now create the map with a specified grid_x and grid_y
    map_editor.create_empty_maps(grid_x, grid_y)
    texture_data = map_editor.get_grid_texture_map()
    tile_type_data = map_editor.get_grid_tile_type_map()

camera.set_tile_type_map(tile_type_data)
camera.set_grid_texture_map(texture_data)


# ---------- gui components ------------
texture_selection_scroller = ScrollableFrameIconButtonArray(scrollable_x_pos, scrollable_y_pos
                                                            , scrollable_x_length, scrollable_y_length, 3, 4)
image_x_length, image_y_length = texture_selection_scroller.get_required_image_dimensions()
forest_tiles = texture_id_manager.get_category("forest")
active_texture_icons = {}
for key in forest_tiles:
    button_icon = Icon(image_x_length, image_y_length, forest_tiles[key])
    active_texture_icons[key] = button_icon
    texture_selection_scroller.add_button(button_icon, key)
obama = pygame.image.load(os.path.join(definitions.ROOTDIR, "src\\gui\\images\\test_images", "barrack_obama.png"))
obama_icon = Icon(image_x_length, image_y_length, obama)
texture_selection_scroller.set_default_image(obama_icon)



# ---- pygame main loop -----
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    if mode == "TEXTURE_MODE":
        camera.disable_tile_type_viewing()
    if mode == "TILE_TYPE_MODE":
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

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if texture_selection_scroller.check_inside(mouse_x, mouse_y):
                curr_texture = texture_selection_scroller.click(mouse_x, mouse_y)
            else:
                curr_grid_pos = camera.click_tile(mouse_x, mouse_y)
                if curr_grid_pos:
                    map_editor.update_tile_texture_id(curr_grid_pos[0], curr_grid_pos[1], curr_texture)

    screen.fill((0, 0, 0))
    camera.set_grid_texture_map(map_editor.get_grid_texture_map())
    camera.set_tile_type_map(map_editor.get_grid_tile_type_map())
    camera.set_center(camera_x_center, camera_y_center)
    camera.render(screen)

    if curr_texture:
        active_texture_icons[curr_texture].render(screen, curr_texture_icon_x, curr_texture_icon_y)
    else:
        obama_icon.render(screen, curr_texture_icon_x, curr_texture_icon_y)
    texture_selection_scroller.render(screen)

    pygame.display.update()

map_save_load.save(file_name)