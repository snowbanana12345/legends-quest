import os
import pygame
import definitions

root = definitions.ROOTDIR
class MapIdManager:
    def __init__(self):
        self.id_texture_map = {}
        self.id_texture_map["forest_fresh_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "fresh_grass.png"))
        self.id_texture_map["forest_short_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "short_grass.png"))
        self.id_texture_map["forest_thick_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "thick_grass.png"))

    def get_map_tile(self, key):
        return self.id_texture_map[key]