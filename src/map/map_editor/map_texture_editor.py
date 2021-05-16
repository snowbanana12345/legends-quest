class MapTextureEditor:
    def __init__(self, x_length, y_length):
        self.grid_texture_map = {}
        self.x_length = x_length
        self.y_length = y_length

    def set_default_texture(self):
        for i in range(1, self.x_length + 1):
            for j in range(1, self.y_length + 1):
                self.grid_texture_map[(i,j)] = None

    def update_tile(self, xpos, ypos, key):
        self.grid_texture_map[(xpos, ypos)] = key

    def set_grid_texture_map(self, grid_texture_map):
        self.grid_texture_map = grid_texture_map

    def get_grid_texture_map(self, grid_texture_map):
        return self.grid_texture_map

