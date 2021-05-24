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