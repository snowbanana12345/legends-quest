import pygame

"""
This class is a camera!
"""
class MapTextureRenderer:
    def __init__(self, x_pixels, y_pixels, xcenter, ycenter, camera_box_width, camera_box_height):
        self.x_pixels = x_pixels # x size of the map display
        self.y_pixels = y_pixels # y size of the map display
        self.camera_box_width = camera_box_width
        self.camera_box_height = camera_box_height
        self.x_center = xcenter # center of the camera
        self.y_center = ycenter # center of the camera
        self.grid_texture_id_map = None
        self.grid_texture_map = None
        self.move_velocity = 5


    def set_grid_texture_map(self, grid_texture_id_map):
        self.grid_texture_id_map = grid_texture_id_map
        for key in grid_texture_id_map:
            

    def scale_texture_maps(self):
        for grid_coord in self.grid_texture_map:
            image = self.grid_texture_map[grid_coord]
            if image is not None:
                self.grid_texture_map[grid_coord] = pygame.transform.smoothscale(image, (self.camera_box_width, self.camera_box_height))

    def render(self, screen):
        pass





