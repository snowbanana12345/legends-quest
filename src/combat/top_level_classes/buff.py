"""
Abstract class Buff.
A Debuff can be implemented using this class as well
It contains tick damage to model damage over time
It contains stat modifiers to model a buff/debuff
"""

class Buff:
    def __init__(self):
        self.duration = 0
        self.tick_damage = None
        self.combat_stat_modifier = None
        self.name = ""

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_tick_damage(self):
        return self.tick_damage

    def get_combat_stat_modifier(self):
        return self.combat_stat_modifier
