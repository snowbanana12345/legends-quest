import math

from src.gui.code.unit_buttons.box import Box
from src.gui.code.unit_buttons.image_with_frame import ImageWithFrame

"""
Example :
x_divisions = 4
y_divisions = 3
this creates an array of image and gui_backgrounds that is 4 x 3 images

self.pointer points at the top row of images
self.pointer = 1 implies that the top row are images, 5,6,7,8
self.pointer = 2 implies that the top row are images 9,10,11,12
"""
class ScrollableFrameIconButtonArray(Box):
    def __init__(self, xpos, ypos, xlength, ylength, x_divisions, y_divisions):
        super().__init__(xpos, ypos, xlength, ylength)
        self.pointer = 0
        self.pointer_limit = 0
        self.image_number = 0
        self.button_number_id_map = {}
        self.button_number_image_with_frame_map = {}
        self.images_width = xlength / x_divisions
        self.images_height = ylength / y_divisions
        self.x_divisions = x_divisions
        self.y_divisions = y_divisions
        self.default_image_with_frame = None

    def get_required_image_dimensions(self):
        return (self.images_width, self.images_height)

    def set_default_image_with_frame(self, image_with_frame):
        self.default_image_with_frame = image_with_frame

    def add_button(self, renderable, button_id):
        if self.check_id_already_used(button_id):
            print("Warning! : duplicate button ids")
        self.image_number += 1
        self.button_number_id_map[self.image_number] = button_id
        self.button_number_image_with_frame_map[self.image_number] = renderable
        self.pointer_limit = max(0, math.ceil(self.image_number / self.x_divisions) - 2)

    def check_id_already_used(self, new_button_id):
        for image_number in self.button_number_id_map:
            if self.button_number_id_map == new_button_id:
                return True
        return False

    def move_pointer_down(self):
        if self.pointer >= self.pointer_limit:
            return None
        self.pointer += 1

    def move_pointer_up(self):
        if self.pointer <= 0:
            return None
        self.pointer -= 1

    """
    This functions returns the user specified button id when it is clicked 
    """
    def click(self, mouse_x, mouse_y):
        if not self.check_inside(mouse_x, mouse_y):
            return None
        relative_x_position = mouse_x - self.xpos
        relative_y_position = mouse_y - self.ypos
        image_number = int(relative_x_position / self.images_width) + 1
        image_number += int(relative_y_position / self.images_height)*self.x_divisions
        image_number += self.pointer*self.x_divisions
        if image_number > self.image_number: # this happens when the number of images is not divisible by self.x_divisions
            return None
        return self.button_number_id_map[image_number]

    def render(self, screen):
        for index_y in range(self.y_divisions):
            for index_x in range(self.x_divisions):
                image_x_pos = self.xpos + index_x * self.images_width
                image_y_pos = self.ypos + index_y * self.images_height
                image_number = (index_x + 1) + (index_y + self.pointer) * self.x_divisions
                if image_number <= self.image_number:
                    image_with_frame = self.button_number_image_with_frame_map[image_number]
                    image_with_frame.render(screen, image_x_pos, image_y_pos)
                elif self.default_image_with_frame is not None:
                    self.default_image_with_frame.render(screen, image_x_pos, image_y_pos)




