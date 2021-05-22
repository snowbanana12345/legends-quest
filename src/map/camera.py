import pygame
from src.map.texture_id_manager import TextureIdManager

"""
This class is a camera!
"""
class Camera:
    def __init__(self, x_pixels, y_pixels, xcenter, ycenter, camera_grid_x_length, camera_grid_y_length, texture_id_manager):
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

        # tile type variables
        self.tile_type_map = {}
        self.tile_type_viewing = True
        self.tile_type_colors = {
            "INVALID" : (255, 0, 0),
            "VALID" : (0, 255, 0)
        }

        self.texture_id_manager = texture_id_manager

        # draw grid line variables
        self.grid_viewing = True
        self.grid_line_color = (255,255,255)
        self.grid_line_width = 5
    """
    Call this function to continuously update the center of the camera
    """
    def set_center(self, new_x_center, new_y_center):
        self.x_center = new_x_center
        self.y_center = new_y_center

    def set_grid_line_width(self, line_width):
        self.grid_line_width = line_width

    """
    this functions returns the tile number that is clicked
    """
    def click_tile(self, mouse_x, mouse_y):
        world_x_coord = int(self.x_center - self.x_pixels / 2 + mouse_x)
        world_y_coord = int(self.y_center - self.y_pixels / 2 + mouse_y)
        grid_x_coord = world_x_coord // self.camera_grid_x_length
        grid_y_coord = world_y_coord // self.camera_grid_y_length
        if 0<=grid_x_coord<=self.grid_coord_x_max and 0<=grid_y_coord<=self.grid_coord_y_max:
            return (grid_x_coord, grid_y_coord)
        else:
            return None

    # load all of the image files onto this class and scale them appropriately
    # DO NOT update grid_x_coord and grid_y_coord and scale again, this will blur the images
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

    def update_texture(self, grid_pos, new_texture_key):
        self.grid_texture_id_map[grid_pos] = new_texture_key
        new_texture_image = self.texture_id_manager.get_map_tile(new_texture_key)
        scaled_new_texture_image = self.scale_texture_image(new_texture_image)
        self.grid_texture_map[grid_pos] = scaled_new_texture_image

    def set_tile_type_map(self, tile_type_map):
        self.tile_type_map = tile_type_map

    def enable_tile_type_viewing(self):
        self.tile_type_viewing = True

    def disable_tile_type_viewing(self):
        self.tile_type_viewing = False

    def scale_texture_image(self, texture_image):
        return pygame.transform.smoothscale(texture_image, (self.camera_grid_x_length, self.camera_grid_y_length))

    def scale_texture_maps(self):
        for grid_coord in self.grid_texture_map:
            image = self.grid_texture_map[grid_coord]
            if image is not None:
                self.grid_texture_map[grid_coord] = self.scale_texture_image(image)

    """
    This class renders as many tiles that could fit onto the screen
    The world coordinate system that the camera sees is implicitly defined by the grid and the grid_x_length and the grid_y_length
    """
    def render(self, screen):
        # find the grid coordinates of the extreme end tiles tile that are just outside the screen
        # or are partially inside the screen
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

        # render all the grids
        for grid_coord_x in range(curr_top_left_grid_x, curr_bottom_right_grid_x + 1):
            for grid_coord_y in range(curr_top_left_grid_y, curr_bottom_right_grid_y + 1):
                # create the tile image
                image_screen_x_coord = grid_coord_x * self.camera_grid_x_length - self.x_center + self.x_pixels / 2
                image_screen_y_coord = grid_coord_y * self.camera_grid_y_length - self.y_center + self.y_pixels / 2
                image = self.grid_texture_map[(grid_coord_x, grid_coord_y)]
                if image is None: # draw a grey box to indicate the absence of a image
                    pygame.draw.rect(screen, (128, 128, 128), (image_screen_x_coord, image_screen_y_coord
                                                               , self.camera_grid_x_length, self.camera_grid_y_length))
                else :
                    screen.blit(image, (image_screen_x_coord, image_screen_y_coord))
                # if tile type viewing is enabled view the tile type
                if self.tile_type_viewing:
                    tile_type = self.tile_type_map[(grid_coord_x, grid_coord_y)]
                    tile_type_color = self.tile_type_colors[tile_type]
                    transparent_surface = pygame.Surface((self.camera_grid_x_length // 4, self.camera_grid_y_length // 4))
                    tile_type_x_coord = image_screen_x_coord + (self.camera_grid_x_length // 8) * 3
                    tile_type_y_coord = image_screen_y_coord + (self.camera_grid_y_length // 8) * 3
                    transparent_surface.fill(tile_type_color)
                    screen.blit(transparent_surface, (tile_type_x_coord, tile_type_y_coord))

        if self.grid_viewing:
            # world coordinates of the boundary grid points
            grid_boundary_x_coords = [grid_x * self.camera_grid_x_length - self.x_center + self.x_pixels / 2
                                      for grid_x in range(curr_top_left_grid_x, curr_bottom_right_grid_x + 2)]
            grid_boundary_y_coords = [grid_y * self.camera_grid_y_length - self.y_center + self.y_pixels / 2
                                      for grid_y in range(curr_top_left_grid_y, curr_bottom_right_grid_y + 2)]

            # draw vertical grid lines
            for grid_boundary_x_coord in grid_boundary_x_coords:
                pygame.draw.line(screen, self.grid_line_color, (grid_boundary_x_coord, grid_boundary_y_coords[0])
                                 , (grid_boundary_x_coord, grid_boundary_y_coords[-1]), width = self.grid_line_width)

            # draw horizontal grid lines
            for grid_boundary_y_coord in grid_boundary_y_coords:
                pygame.draw.line(screen, self.grid_line_color, (grid_boundary_x_coords[0],grid_boundary_y_coord)
                                 , (grid_boundary_x_coords[-1], grid_boundary_y_coord), width=self.grid_line_width)



