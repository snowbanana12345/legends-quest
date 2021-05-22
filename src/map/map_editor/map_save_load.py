import os
import pickle
import definitions


class MapSaveLoad:
    def __init__(self):
        self.working_folder = os.path.join(definitions.ROOTDIR, "data\\game_data\\maps")
        self.grid_texture_id_map = {}
        self.grid_tile_type_map = {}
        self.file_extension = ".txt"
        self.separator_string = "[]"

    def set_grid_texture_id_map(self, texture_id_map):
        self.grid_texture_id_map = texture_id_map

    def get_grid_texture_id_map(self):
        return self.grid_texture_id_map

    def get_copy_grid_texture_id_map(self):
        return self.grid_texture_id_map.copy()

    def set_grid_tile_type_map(self, tile_type_map):
        self.grid_tile_type_map = tile_type_map

    def get_grid_tile_type_map(self):
        return self.grid_tile_type_map

    def get_copy_grid_tile_type_map(self):
        return self.grid_tile_type_map.copy()

    def save(self, file_name):
        file_path = os.path.join(self.working_folder, file_name)
        with open(file_path, "w") as map_data_file:
            for grid_coord in self.grid_texture_id_map:
                map_data_file.write(str(grid_coord[0]) + self.separator_string)
                map_data_file.write(str(grid_coord[1]) + self.separator_string)
                texture_id = self.grid_texture_id_map[grid_coord] if self.grid_texture_id_map[grid_coord] else "forest_fresh_grass"
                map_data_file.write(str(texture_id) + self.separator_string)
                tile_type = self.grid_tile_type_map[grid_coord] if self.grid_tile_type_map[grid_coord] else "VALID"
                map_data_file.write(str(tile_type) + "\n")

    def pickle_save(self, file_name): # file name must have the extension .pickle
        pickle_file_path = os.path.join(self.working_folder, file_name)
        with open(pickle_file_path, "wb") as pickle_out:
            pickle.dump(self, pickle_out)

    """
    returns the loaded map_save_load file if it exists else returns None
    """
    @staticmethod
    def pickle_load(pickle_file_path):
        if not os.path.exists(pickle_file_path):
            return None
        with open(pickle_file_path, "rb") as pickle_in:
            return pickle.load(pickle_in)

    """
    loads a file from inside the working folder
    """
    def load(self, file_name):
        file_path = os.path.join(self.working_folder, file_name)
        if os.stat(file_path).st_size == 0:
            return False
        with open(file_path, "r") as map_data_file:
            for line in map_data_file:
                if line == "\n":
                    continue
                line_data = line.split(self.separator_string)
                grid_coord_x = int(line_data[0])
                grid_coord_y = int(line_data[1])
                texture_id = line_data[2]
                tile_type = line_data[3]
                self.grid_texture_id_map[(grid_coord_x, grid_coord_y)] = texture_id
                self.grid_tile_type_map[(grid_coord_x, grid_coord_y)] = tile_type

        # ---- clean up the file ------
        for grid_pos in self.grid_tile_type_map:
            self.grid_tile_type_map[grid_pos] = self.grid_tile_type_map[grid_pos].replace("\n","")
        return True
