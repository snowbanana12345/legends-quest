from src.combat.skills.enemy_skills.scratch import Scratch
from src.combat.top_level_classes.combat_stats_types import CombatStatsTypes
from src.combat.top_level_classes.combat_stats import CombatStats
from src.combat.top_level_classes.enemy import Enemy
from src.combat.top_level_classes.enemy_types import EnemyTypes


class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = EnemyTypes.UNDEAD
        self.experience = 50
        self.skills[1] = Scratch()
        self.combat_stats = CombatStats()
        self.combat_stats.set_combat_stat(CombatStatsTypes.HEALTH, 20)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MAX_HEALTH, 20)
        self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA, 30)
        self.combat_stats.set_combat_stat(CombatStatsTypes.MAX_STAMINA, 30)
        self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA_REGEN, 10)
        self.combat_stats.set_combat_stat(CombatStatsTypes.SPEED, 10)