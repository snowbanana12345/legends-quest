import os
import pygame
import definitions

root = definitions.ROOTDIR
"""
Manages iding of texture files
DO NOT use space separated strings or special symbols as keys!!!
"""
class TextureIdManager:
    def __init__(self):
        self.category_map = {}
        forest_id_texture_map = {}
        forest_id_texture_map["fresh_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "fresh_grass.png"))
        forest_id_texture_map["short_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "short_grass.png"))
        forest_id_texture_map["thick_grass"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "thick_grass.png"))
        forest_id_texture_map["autumn_forest"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "autumn_forest.png"))
        forest_id_texture_map["dark_forest"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "dark_forest.png"))
        forest_id_texture_map["enchanted_forest"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "enchanted_forest.png"))
        forest_id_texture_map["light_forest"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "light_forest.png"))
        forest_id_texture_map["light_rocks"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "light_rocks.png"))
        forest_id_texture_map["muddy_road"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "muddy_road.png"))
        forest_id_texture_map["thick_forest"] = pygame.image.load(os.path.join(root, "assets\\map_tiles\\forest", "thick_forest.png"))
        self.category_map["forest"] = forest_id_texture_map

    def get_map_tile_by_category(self, category, key):
        return self.category_map[category][key]

    def get_category(self, category):
        return self.category_map[category]

    def catenate_category_key(self, category, key):
        return category + "_" + key

    """
    This functions assumes that the format of the key is "{category}_{key}"
    """
    def get_map_tile(self, key):
        if key is None:
            return None
        key_dat = key.split("_")
        category = key_dat[0]
        key = ""
        for i in range(1, len(key_dat)):
            key += key_dat[i]
            if i != len(key_dat) - 1:
                key += "_"
        return self.category_map[category][key]