from legends_quest_texture_id_manager import TextureIdManager
from legends_quest_map_renderer import MapRenderer


class Map:
    def __init__(self):
        # internal data structures
        self.player_x_coordinate = None
        self.player_y_coordinate = None
        self.box_width = None      # width of each box
        self.box_height = None     # height of each box
        self.velocity = None
        self.map_data = {}
        self.tile_types = {}

        # helper models
        self.texture_id_manager = TextureIdManager()    # stores the textures used in the map
        self.map_renderer = MapRenderer()    # convert game coordinates to screen coordinates

    def move_up(self):
        # Move player up 1 box, if the box is valid.
        current_box = self.get_current_box()
        new_box = self.get_above_box(current_box)
        if self.tile_types[new_box] == "VALID":
            self.player_y_coordinate -= self.velocity

    def move_down(self):
        # Move player down 1 box, if the box is valid.
        current_box = self.get_current_box()
        new_box = self.get_below_box(current_box)
        if self.tile_types[new_box] == "VALID":
            self.player_y_coordinate += self.velocity

    def move_left(self):
        # Move player left 1 box, if the box is valid.
        current_box = self.get_current_box()
        new_box = self.get_left_box(current_box)
        if self.tile_types[new_box] == "VALID":
            self.player_x_coordinate -= self.velocity

    def move_right(self):
        # Move player right 1 box, if the box is valid
        current_box = self.get_current_box()
        new_box = self.get_right_box(current_box)
        if self.tile_types[new_box] == "VALID":
            self.player_x_coordinate += self.velocity

    def get_current_box(self):
        """
         obtains the current box which the player is at, based on player's
         global x and y coordinates
        """
        box_x_coordinate = self.player_x_coordinate // self.box_width
        box_y_coordinate = self.player_y_coordinate // self.box_height
        return box_x_coordinate, box_y_coordinate

    @staticmethod
    def get_above_box(current_box):
        # Returns the box above the player's current box.
        current_box_x_coordinate = current_box[0]
        current_box_y_coordinate = current_box[1]

        return current_box_x_coordinate, current_box_y_coordinate + 1

    @staticmethod
    def get_below_box(current_box):
        # Returns the box below the player's current box.
        current_box_x_coordinate = current_box[0]
        current_box_y_coordinate = current_box[1]

        return current_box_x_coordinate, current_box_y_coordinate - 1

    @staticmethod
    def get_left_box(current_box):
        # Returns the box to the left of the player's current box.
        current_box_x_coordinate = current_box[0]
        current_box_y_coordinate = current_box[1]

        return current_box_x_coordinate - 1, current_box_y_coordinate

    @staticmethod
    def get_right_box(current_box):
        # Returns the box to the right of the player's current box.
        current_box_x_coordinate = current_box[0]
        current_box_y_coordinate = current_box[1]

        return current_box_x_coordinate + 1, current_box_y_coordinate

    def assign_data_structures(self, list_of_data):
        """ Assign structures to each internal variable
        """
        self.player_x_coordinate = list_of_data[0]
        self.player_y_coordinate = list_of_data[1]
        self.box_width = list_of_data[2]
        self.box_height = list_of_data[3]
        self.velocity = list_of_data[5]
        self.map_data = list_of_data[5]
        self.tile_types = list_of_data[6]
