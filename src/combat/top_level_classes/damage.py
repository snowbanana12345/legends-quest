from src.combat.top_level_classes.data_struct import DataStruct


class Damage(DataStruct):
    def __init__(self):
        super().__init__()

    def set_damage(self, damage_type, damage):
        self.set_data(damage_type, damage)

    def get_damage(self, damage_type):
        return self.get_data(damage_type)