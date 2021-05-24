"""
Abstract class skill, used only in the calculation of hit(skill) method in CombatUnit class
A generate skill can apply buffs or debuffs
Healing skills can be implemented by doing negative PURE damage

Since this class only holds information, it only needs to be instantiated once in some ID manager
All variables in this class should be FINAL.
"""

class Skill:
    def __init__(self):
        self.damage = None
        self.buffs = []
        self.skill_costs = None
        self.range = 0

    def get_skill_costs(self):
        return self.skill_costs