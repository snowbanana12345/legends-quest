import pygame

class MapTextureRenderer:
    def __init__(self, x_pixels, y_pixels, division):
        self.x_pixels = x_pixels # x size of the map display
        self.y_pixels = y_pixels # y size of the map display
        self.division = division # the size of each division
        self.x_top_left = 0 # top left coordinates of the screen
        self.y_top_left = 0 # top right coordinates of the screen
        self.grid_texture_map = None
        self.move_velocity = 5


    def set_grid_texture_map(self, grid_texture_map):
        self.grid_texture_map = grid_texture_map

    def scale_texture_maps(self):
        for grid_coord in self.grid_texture_map:
            image = self.grid_texture_map[grid_coord]
            if image is not None:
                self.grid_texture_map[grid_coord] = pygame.transform.smoothscale(image, (self.division, self.division))

    def render(self, screen):
        pass





