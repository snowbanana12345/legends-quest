import pygame

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

grid_x = 1000
grid_y = 1000
file_name = "tutorial_island_forest"

# ----- initialize classes -----
texture_id_manager = TextureIdManager()
map_save_load = MapSaveLoad()
camera = Camera(screen_width, screen_height, camera_x_center, camera_y_center
                , world_grid_x_length, world_grid_y_length, texture_id_manager)
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
texture_selection_scroller = ScrollableFrameIconButtonArray(700, 400, 300, 400, 3, 4)
image_x_length, image_y_length = texture_selection_scroller.get_required_image_dimensions()
forest_tiles = texture_id_manager.get_category("forest")
for key in forest_tiles:
    button_icon = Icon(image_x_length, image_y_length, forest_tiles[key])
    texture_selection_scroller.add_button(button_icon, key)


# ---- pygame main loop -----
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    texture_selection_scroller.render(screen)
    pygame.display.update()

map_save_load.save(file_name)