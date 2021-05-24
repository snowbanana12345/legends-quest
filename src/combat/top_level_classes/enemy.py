from src.combat.top_level_classes.combat_unit import CombatUnit


"""
Abstract class for enemy
The relevant information this class holds is the skills the enemy can use,
The type of the enemy, e.g. undead, demon, human 
Combat stats such as health, mana, etc.
Loot and experience gain from this enemy

Note : this class only contains information relevant to the combat logic
information related to rendering and animation should be delegated to another class
"""

class Enemy(CombatUnit):
    def __init__(self):
        super().__init__()
        self.enemy_type = None
        self.experience = 0
        self.loot_generator = None






