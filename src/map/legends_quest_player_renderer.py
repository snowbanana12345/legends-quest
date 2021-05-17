import pygame


class PlayerTextureRenderer:
    def __init__(self, width, height, player_images):
        # internal data structures
        self.width = width
        self.height = height
        self.player_images = player_images

        # for rendering player movement
        self.use_image_list = []
        self.is_moving = False
        self.animation_counter = 0
        self.max_animation_counter = len(self.player_images['North']) * 3

    def render(self, screen):
        """
        Main function for the class. Renders the player image
        depending on whether the player is moving or not.
        """
        # Increase animation counter if character is moving
        self.move()

        # Displays the current player image at the center of the screen
        x_coordinate = (screen.get_width() - self.width) / 2
        y_coordinate = (screen.get_height() - self.height) / 2
        image = self.use_image_list[self.animation_counter // 3]
        screen.blit(image, (x_coordinate, y_coordinate))

    def scale_player_textures(self):
        """ Scales each image file to the right width and height
        """
        # Define scaling function
        def scale_fn(image):
            return pygame.transform.smoothscale(image, (self.width, self.height))
        # Apply function to each image in player_images.
        self.player_images = {direction: list(map(scale_fn, self.player_images[direction]))
                              for direction in self.player_images.keys()}

    def start_moving(self):
        self.is_moving = True

    def stop_moving(self):
        self.is_moving = False
        # Reset animation counter to 0 so that a image of a static player would be used.
        self.animation_counter = 0

    def face_north(self):
        self.use_image_list = self.player_images["North"]

    def face_south(self):
        self.use_image_list = self.player_images["South"]

    def face_east(self):
        self.use_image_list = self.player_images["East"]

    def face_west(self):
        self.use_image_list = self.player_images["West"]

    def move(self):
        """
        Increases the animation counter so that the player will appear to move
        when called together with render.
        """
        if self.is_moving:
            self.animation_counter += 1
            # Reset animation counter to cycle through list of images again
            if self.animation_counter >= self.max_animation_counter - 1:
                self.animation_counter = 0
