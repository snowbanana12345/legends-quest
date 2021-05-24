from src.combat.top_level_classes.combat_unit import CombatUnit

"""
This class is responsible for converting the information in hero class to information
relevant to combat
"""
class HeroCombat(CombatUnit):
    def __init__(self):
        super().__init__()

    """
    hero is the hero object
    """
    def configure(self, hero):
        pass
