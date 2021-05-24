from src.combat.top_level_classes.data_struct import DataStruct


class SkillCost(DataStruct):
    def __init__(self):
        super().__init__()

    def set_skill_cost(self, cost_type, cost):
        self.set_data(cost_type, cost)

    def get_skill_cost(self, cost_type):
        return self.get_skill_cost(cost_type)
