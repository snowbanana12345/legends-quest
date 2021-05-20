import pygame
import os

from src.map.camera import Camera
from src.map.legends_quest_player_renderer import PlayerTextureRenderer
from src.map.texture_id_manager import TextureIdManager

title = "Map Test"
screen_width = 1000
screen_height = 800
frame_rate = 60

camera_x_center = 0
camera_y_center = 0
world_grid_x_length = 300
world_grid_y_length = 300
camera_velocity = 10

pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# world coordinates are x = 0 to x = 1200, y = 0 to y = 1200
grid_texture_id_map = {(0, 0): "forest_fresh_grass", (1, 0): "forest_short_grass", (2, 0): "forest_short_grass",
                       (3, 0): "forest_thick_grass", (0, 1): "forest_thick_grass", (1, 1): "forest_fresh_grass",
                       (2, 1): "forest_short_grass", (3, 1): "forest_thick_grass", (0, 2): "forest_short_grass",
                       (1, 2): "forest_fresh_grass", (2, 2): "forest_short_grass", (3, 2): "forest_fresh_grass",
                       (0, 3): "forest_thick_grass", (1, 3): "forest_thick_grass", (2, 3): "forest_thick_grass",
                       (3, 3): "forest_fresh_grass"}

grid_tile_type_map = {(0, 0): "INVALID", (1, 0): "INVALID", (2, 0): "INVALID",
                       (3, 0): "INVALID", (0, 1): "INVALID", (1, 1): "VALID",
                       (2, 1): "INVALID", (3, 1): "INVALID", (0, 2): "INVALID",
                       (1, 2): "VALID", (2, 2): "VALID", (3, 2): "INVALID",
                       (0, 3): "VALID", (1, 3): "VALID", (2, 3): "INVALID",
                       (3, 3): "INVALID"}

test_camera = Camera(screen_width, screen_height, camera_x_center, camera_y_center,
                     world_grid_x_length, world_grid_y_length, TextureIdManager())
test_camera.set_grid_texture_map(grid_texture_id_map)
test_camera.set_tile_type_map(grid_tile_type_map)

# For testing PlayerTextureRenderer
north_images = [pygame.image.load(f".\\map\\images\\N{i}.png") for i in range(3)]
east_images = [pygame.image.load(f".\\map\\images\\E{i}.png") for i in range(3)]
west_images = [pygame.image.load(f".\\map\\images\\W{i}.png") for i in range(3)]
south_images = [pygame.image.load(f".\\map\\images\\S{i}.png") for i in range(3)]
test_player = PlayerTextureRenderer(100, 100, {"North": north_images,
                                               "East": east_images,
                                               "West": west_images,
                                               "South": south_images})
test_player.scale_player_textures()
test_player.use_image_list = test_player.player_images["South"]

while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        test_player.start_moving()
        test_player.face_north()
        camera_y_center -= camera_velocity
    if keys[pygame.K_s]:
        test_player.start_moving()
        test_player.face_south()
        camera_y_center += camera_velocity
    if keys[pygame.K_a]:
        test_player.start_moving()
        test_player.face_west()
        camera_x_center -= camera_velocity
    if keys[pygame.K_d]:
        test_player.start_moving()
        test_player.face_east()
        camera_x_center += camera_velocity
    if all([not keys[pygame.K_w], not keys[pygame.K_s], not keys[pygame.K_a], not keys[pygame.K_d]]):
        test_player.stop_moving()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()


    screen.fill((0, 0, 0))
    test_camera.set_center(camera_x_center, camera_y_center)
    test_camera.render(screen)
    test_player.render(screen)
    clock.tick(frame_rate)
    pygame.display.update()
