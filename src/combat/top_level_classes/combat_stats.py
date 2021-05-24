"""
This class behaves as a struct class

"""
from src.combat.top_level_classes.data_struct import DataStruct


class CombatStats(DataStruct):
    def __init__(self):
        super().__init__()

    def set_combat_stat(self, combat_stat_type, amount):
        self.set_data(combat_stat_type, amount)

    def get_combat_stat(self, combat_stat_type):
        return self.get_data(combat_stat_type)
