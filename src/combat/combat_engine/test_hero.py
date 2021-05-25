"""
Level 1 noob with only the skill punch
used purely for testing purposes
"""
from src.combat.skills.hero_skills.punch import Punch
from src.combat.top_level_classes.combat_stats_types import CombatStatsTypes
from src.combat.top_level_classes.combat_stats import CombatStats
from src.combat.top_level_classes.hero_combat import HeroCombat


class Noob(HeroCombat):
    def __init__(self):
        super().__init__()
        self.skills[1] = Punch()
        self.combat_stats = CombatStats()
        self.combat_stats.set_combat_stat(CombatStatsTypes.HEALTH, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MAX_HEALTH, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MANA, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MAX_MANA, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MAX_STAMINA, 100)
        self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA_REGEN, 10)
        self.combat_stats.set_combat_stat(CombatStatsTypes.SPEED, 50)





