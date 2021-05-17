import os
import definitions

"""
stores a texture map and updates it and saves it
"""
class MapEditor:
    def __init__(self, x_length, y_length):
        self.grid_texture_id_map = {}
        self.grid_tile_type_map = {}
        self.x_length = x_length
        self.y_length = y_length
        self.working_folder = os.path.join(definitions.ROOTDIR, "data\\game_data\\maps")
        self.file_extension = ".txt"
        self.separator_string = "[]"

    def set_up_maps(self):
        for i in range(0, self.x_length):
            for j in range(0, self.y_length):
                self.grid_texture_id_map[(i,j)] = None
                self.grid_tile_type_map[(i,j)] = None

    def update_tile_texture_id(self, xpos, ypos, key):
        self.grid_texture_id_map[(xpos, ypos)] = key

    def update_tile_type(self, xpos, ypos, tile_type):
        self.grid_tile_type_map[(xpos, ypos)] = tile_type

    def get_grid_texture_map(self):
        return self.grid_texture_id_map.copy()

    def get_grid_tile_type_map(self):
        return self.grid_tile_type_map.copy()

    def write(self, file_name):
        file_path = os.path.join(self.working_folder, file_name + self.file_extension)
        with open(file_path, "w") as map_data_file:
            for grid_coord in self.grid_texture_id_map:
                map_data_file.write(str(grid_coord[0]) + self.separator_string)
                map_data_file.write(str(grid_coord[1]) + self.separator_string)
                texture_id = self.grid_texture_id_map[grid_coord] if self.grid_texture_id_map[grid_coord] else "forest_fresh_grass"
                map_data_file.write(str(texture_id) + self.separator_string)
                tile_type = self.grid_tile_type_map[grid_coord] if self.grid_tile_type_map[grid_coord] else "VALID"
                map_data_file.write(str(tile_type) + "\n")

    def load(self, file_name):
        file_path = os.path.join(self.working_folder, file_name + self.file_extension)
        with open(file_path, "w") as map_data_file:
            for line in map_data_file:
                line_data = line.split(self.separator_string)
                grid_coord_x = int(line_data[0])
                grid_coord_y = int(line_data[1])
                texture_id = line_data[2]
                tile_type = line_data[3]
                self.grid_texture_id_map[(grid_coord_x, grid_coord_y)] = texture_id
                self.grid_tile_type_map[(grid_coord_x, grid_coord_y)] = tile_type

