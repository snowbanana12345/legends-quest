from src.combat.top_level_classes.SkillCostTypes import SkillCostTypes
from src.combat.top_level_classes.damage import Damage
from src.combat.top_level_classes.damage_types import DamageTypes
from src.combat.top_level_classes.skill import Skill
from src.combat.top_level_classes.skill_cost import SkillCost

"""
The most basic skill of all legend's quest, it does a damage of 1 which is really the minimum damage any skill can deal
It always costs 1 stamina
"""

class Punch(Skill):
    def __init__(self):
        super().__init__()
        self.name = "punch"
        self.damage = Damage()
        self.damage.set_damage(DamageTypes.PHYSICAL, 1)
        self.skill_costs = SkillCost()
        self.skill_costs.set_skill_cost(SkillCostTypes.STAMINA, 1)
        self.range = 1