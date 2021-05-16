import pygame
from src.map.texture_id_manager import TextureIdManager

"""
This class is a camera!
"""
class MapTextureRenderer:
    def __init__(self, x_pixels, y_pixels, xcenter, ycenter, camera_grid_x_length, camera_grid_y_length):
        self.x_pixels = x_pixels # x size of the map display
        self.y_pixels = y_pixels # y size of the map display
        self.camera_grid_x_length = camera_grid_x_length # the x length of the grid as it will appear on the screen
        self.camera_grid_y_length = camera_grid_y_length # the y length of the grid as it will appear on the scree
        self.x_center = xcenter # camera world coordinate center of the camera
        self.y_center = ycenter # camera world coordinate center of the camera
        self.grid_texture_id_map = {}
        self.grid_texture_map = {}
        self.grid_coord_x_max = 0
        self.grid_coord_y_max = 0
        self.move_velocity = 5

        self.texture_id_manager = TextureIdManager()

    def set_center(self, new_x_center, new_y_center):
        self.x_center = new_x_center
        self.y_center = new_y_center

    def set_grid_texture_map(self, grid_texture_id_map):
        self.grid_texture_id_map = grid_texture_id_map
        for grid_coord in grid_texture_id_map:
            key = self.grid_texture_id_map[grid_coord]
            if grid_coord[0] > self.grid_coord_x_max:
                self.grid_coord_x_max = grid_coord[0]
            if grid_coord[1] > self.grid_coord_y_max:
                self.grid_coord_y_max = grid_coord[1]
            self.grid_texture_map[grid_coord] = self.texture_id_manager.get_map_tile(key)
        self.scale_texture_maps()

    def scale_texture_maps(self):
        for grid_coord in self.grid_texture_map:
            image = self.grid_texture_map[grid_coord]
            if image is not None:
                self.grid_texture_map[grid_coord] = pygame.transform.smoothscale(image, (self.camera_grid_x_length, self.camera_grid_y_length))

    def render(self, screen):
        curr_top_left_grid_x = int((self.x_center - self.x_pixels / 2) // self.camera_grid_x_length)
        curr_top_left_grid_y = int((self.y_center - self.y_pixels / 2) // self.camera_grid_y_length)
        curr_bottom_right_grid_x = int((self.x_center + self.x_pixels / 2) // self.camera_grid_x_length) + 1
        curr_bottom_right_grid_y = int((self.y_center + self.y_pixels / 2) // self.camera_grid_y_length) + 1

        # handle boundary of the edge
        curr_top_left_grid_x = int(max(0, curr_top_left_grid_x))
        curr_top_left_grid_y = int(max(0, curr_top_left_grid_y))
        if curr_bottom_right_grid_x > self.grid_coord_x_max:
            curr_bottom_right_grid_x = int(self.grid_coord_x_max)
        if curr_bottom_right_grid_y > self.grid_coord_y_max:
            curr_bottom_right_grid_y = int(self.grid_coord_y_max)

        for grid_coord_x in range(curr_top_left_grid_x, curr_bottom_right_grid_x + 1):
            for grid_coord_y in range(curr_top_left_grid_y, curr_bottom_right_grid_y + 1):
                image_screen_x_coord = grid_coord_x * self.camera_grid_x_length - self.x_center
                image_screen_y_coord = grid_coord_y * self.camera_grid_y_length - self.y_center
                image = self.grid_texture_map[(grid_coord_x, grid_coord_y)]
                screen.blit(image, (image_screen_x_coord, image_screen_y_coord))




