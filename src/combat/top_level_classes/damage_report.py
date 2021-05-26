from src.combat.top_level_classes.damage import Damage


class DamageReport:
    def __init__(self):
        self.damage = Damage()
        self.buffs = []

    def set_damage(self, damage_type, amount):
        self.damage.set_damage(damage_type, amount)

    def add_buff(self, buff):
        self.buffs.append(buff)

    def get_damage(self):
        return self.damage

    def get_buffs(self):
        return self.buffs
