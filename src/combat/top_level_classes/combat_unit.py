from src.combat.top_level_classes.combat_stats_types import CombatStatsTypes
from src.combat.top_level_classes.SkillCostTypes import SkillCostTypes
from src.combat.top_level_classes.damage_report import DamageReport

"""
Abstract class, combat unit participates in combat
"""
class CombatUnit:
    def __init__(self):
        self.skills = {}
        self.combat_stats = None
        self.alive = True # potentially, can implement revive spells that can bring a dead unit back to life
        self.buffs_dict = {}  # { buff id : buff object }
        self.buff_id = 1
        self.buff_duration_dict = {}  # { buff id : buff remaining duration }

    def get_next_buff_id(self):
        self.buff_id = self.buff_id + 1
        return self.buff_id

    def is_alive(self):
        return self.alive

    def has_skill(self, skill_num):
        return skill_num in self.skills

    def get_skill(self, skill_num):
        return self.skills[skill_num]

    # speed is needed for turn order calculations
    def get_speed(self):
        return self.combat_stats.get_combat_stat(CombatStatsTypes.SPEED)

    """
    Attempts to use a skill with skill_num
    returns True if skill can be used and deducts costs
    returns False if skill cannot be used
    """
    def use_skill(self, skill_num):
        if skill_num not in self.skills:
            return False
        skill = self.skills[skill_num]
        costs = skill.get_skill_costs().get_dictionary()

        # determine if all of the skill costs can be met
        for cost in costs:
            amount = costs[cost]
            if cost == SkillCostTypes.HEALTH:
                curr_health = self.combat_stats.get_combat_stat(CombatStatsTypes.HEALTH)
                if amount >= curr_health:
                    return False
            elif cost == SkillCostTypes.MANA:
                curr_mana = self.combat_stats.get_combat_stat(CombatStatsTypes.MANA)
                if amount >= curr_mana:
                    return False
            elif cost == SkillCostTypes.STAMINA:
                curr_stamina = self.combat_stats.get_combat_stat(CombatStatsTypes.STAMINA)
                if amount >= curr_stamina:
                    return False

        # perform the deductions upon determining that all of the skill costs can be met and use the skill
        for cost in costs:
            amount = costs[cost]
            if cost == SkillCostTypes.HEALTH:
                curr_health = self.combat_stats.get_combat_stat(CombatStatsTypes.HEALTH)
                new_health = curr_health - amount
                self.combat_stats.set_combat_stat(CombatStatsTypes.HEALTH, new_health)
            elif cost == SkillCostTypes.MANA:
                curr_mana = self.combat_stats.get_combat_stat(CombatStatsTypes.MANA)
                new_mana = curr_mana - amount
                self.combat_stats.set_combat_stat(CombatStatsTypes.MANA, new_mana)
            elif cost == SkillCostTypes.STAMINA:
                curr_stamina = self.combat_stats.get_combat_stat(CombatStatsTypes.STAMINA)
                new_stamina = curr_stamina - amount
                self.combat_stats.set_combat_stat(CombatStatsTypes.STAMINA, new_stamina)
        return True


    """
    This method calculates what happens when a monster is hit
    A standard calculation method can be implemented here
    Returns a report on the damage the unit took, and the buffs/debuffs the unit applied 
    """
    def hit(self, skill):
        damage = skill.get_damage()
        damage_report = DamageReport()
        for damage_type in damage.get_damage_types():
            amount = damage.get_damage(damage_type)
            damage_report.set_damage(damage_type, amount)
            self.take_health_damage(amount)
        if self.combat_stats.get_combat_stat(CombatStatsTypes.HEALTH) <= 0:
            self.alive = False

        buffs = skill.get_buffs()
        for buff in buffs:
            new_buff_id = self.get_next_buff_id()
            self.buffs_dict[new_buff_id] = buff
            self.buff_duration_dict[new_buff_id] = buff.get_duration()
            damage_report.add_buff(buff)
        return damage_report

    def take_health_damage(self, amount):
        health = self.combat_stats.get_combat_stat(CombatStatsTypes.HEALTH)
        new_health = health - amount
        self.combat_stats.set_combat_stat(CombatStatsTypes.HEALTH, new_health)

    """
    This method ticks down buff timers
    """
    def tick(self):
        for buff_id in self.buffs_dict:
            buff = self.buffs_dict[buff_id]
            tick_damage = buff.get_tick_damage()
            for damage_type in tick_damage.get_damage_types():
                amount = tick_damage.get_damage(damage_type)
                self.take_health_damage(amount)


