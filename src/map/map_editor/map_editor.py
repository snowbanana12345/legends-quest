import os
import definitions

"""
stores a texture map and updates it and saves it
"""
class MapEditor:
    def __init__(self):
        self.grid_texture_id_map = {}
        self.grid_tile_type_map = {}

    def create_empty_maps(self, grid_x, grid_y):
        for i in range(0, grid_x):
            for j in range(0, grid_y):
                self.grid_texture_id_map[(i,j)] = None
                self.grid_tile_type_map[(i,j)] = "INVALID"

    def update_tile_texture_id(self, xpos, ypos, key):
        self.grid_texture_id_map[(xpos, ypos)] = key

    def update_tile_type(self, xpos, ypos, tile_type):
        self.grid_tile_type_map[(xpos, ypos)] = tile_type

    """
    set its pointer to the texture_id_map to be edited
    """
    def set_grid_texture_id_map(self, texture_id_map):
        self.grid_texture_id_map = texture_id_map

    def set_tile_type_map(self, tile_type_map):
        self.grid_tile_type_map = tile_type_map


    """
    Returns a copy of the grid texture id data
    """
    def get_copy_grid_texture_map(self):
        return self.grid_texture_id_map.copy()

    """
    allows another variable to point to this map
    """
    def get_grid_texture_map(self):
        return self.grid_texture_id_map.copy()

    """
    Returns a copy of the grid type data
    """
    def get_copy_grid_tile_type_map(self):
        return self.grid_tile_type_map.copy()

    """
    allows another variable to point to this map
    """
    def get_grid_tile_type_map(self):
        return self.grid_tile_type_map





