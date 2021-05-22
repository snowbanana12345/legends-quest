import pickle
import os
import definitions

from src.map.map_editor.map_save_load import MapSaveLoad

root_dir = definitions.ROOTDIR
pickle_file_path = os.path.join(root_dir, "data\\game_data\\maps","tutorial_island_forest.pickle")

#map_save_load = MapSaveLoad()
#map_save_load.load("tutorial_island_forest")
#pickle_out = open(pickle_file_path, "wb")
#pickle.dump(map_save_load, pickle_out)
#pickle_out.close()

pickle_in = open(pickle_file_path, "rb")
map_save_load = pickle.load(pickle_in)
print(map_save_load)