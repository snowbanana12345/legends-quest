from src.gui.code.unit_buttons.box import Box


class ScrollableFrameIconButtonArray(Box):
    def __init__(self, xpos, ypos, xlength, ylength, x_divisions, y_divisions):
        super().__init__(xpos, ypos, xlength, ylength)
        self.buttons = []
        self.pointer = 0
        self.image_number = 0

    def add_button(self, image, frame_image, button_id):
        pass

    def click(self, mouse_x, mouse_y):
        if not self.check_inside(mouse_x, mouse_y):
            return None

    