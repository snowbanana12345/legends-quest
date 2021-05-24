from src.combat.top_level_classes.CombatStatsTypes import CombatStatsTypes
from src.combat.top_level_classes.SkillCostTypes import SkillCostTypes

"""
Abstract class, combat unit participates in combat
"""
class CombatUnit:
    def __init__(self):
        self.skills = {}
        self.combat_stats = None
        self.alive = True # potentially, can implement revive spells that can bring a dead unit back to life
        self.buffs = []

    def is_alive(self):
        return self.alive

    """
    Attempts to use a skill with skill_num
    returns True if skill can be used and deducts costs
    returns False if skill cannot be used
    """
    def use_skill(self, skill_num):
        if skill_num not in self.skills:
            return False
        skill = self.skills[skill_num]
        costs = skill.get_skill_costs()
        for cost in costs:
            amount = costs[cost]
            if cost == SkillCostTypes.HEALTH:
                curr_health = self.combat_stats.get_combat_stat(CombatStatsTypes.HEALTH)
                if amount >= curr_health:
                    return False
                else :
                    new_health = curr_health - amount
                    self.combat_stats.set_combat_stat(CombatStatsTypes.HEALTH, new_health)
            elif cost == SkillCostTypes.MANA:
                curr_mana = self.combat_stats.get_combat_stat(CombatStatsTypes.MANA)
                if amount >= curr_mana:
                    return False
                else :
                    new_mana = curr_mana - amount
                    self.combat_stats.set_combat_stat(CombatStatsTypes.MANA, new_mana)
            elif cost == SkillCostTypes.STAMINA:
                curr_stamina = self.combat_stats.get_combat_stat(CombatStatsTypes.STAMINA)
                if amount >= curr_stamina:
                    return False
                else :
                    new_stamina = curr_stamina - amount
                    self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA, new_stamina)
        return True


    """
    This method calculates what happens when a monster is hit
    A universal calculation method can be implemented here
    """
    def hit(self, skill):
        pass


