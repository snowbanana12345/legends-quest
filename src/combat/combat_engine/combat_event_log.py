from src.combat.combat_engine.combat_events.combat_event_types import CombatEventTypes
from src.combat.top_level_classes.damage_types import DamageTypes


class CombatEventLog:
    def __init__(self):
        self.event_log = []
        self.damage_type_to_string = {
            DamageTypes.PHYSICAL : "Physical",
            DamageTypes.COLD : "Cold",
            DamageTypes.FIRE : "Fire",
            DamageTypes.CHAOS : "Chaos",
            DamageTypes.LIGHTNING : "Lightning",
            DamageTypes.PURE : "Pure",
        }

    def log_use_skill_event(self, user_name, target_name, skill, damage_report):
        new_log = (CombatEventTypes.USE_SKILL, user_name, target_name, skill, damage_report)
        self.event_log.append(new_log)

    def log_move_event(self, unit_name, old_position, new_position):
        new_log = (CombatEventTypes.MOVE, unit_name, old_position, new_position)
        self.event_log.append(new_log)

    def log_add_unit_event(self, unit_name, position):
        new_log = (CombatEventTypes.ADD, unit_name, position)
        self.event_log.append(new_log)

    def event_to_string_message(self, log):
        string_message = ""
        if log[0] == CombatEventTypes.USE_SKILL:
            string_message += log[1] + " used "
            string_message += log[2].get_name() + " on "
            string_message += log[3] + " dealing "
            damage_report = log[4]
            damage = damage_report.get_damage()
            for damage_type in damage.get_damage_types():
                amount = damage.get_damage(damage_type)
                string_message += str(amount) + " " + self.damage_type_to_string[damage_type] + " "
            string_message += " and applying "
            buffs = damage_report.get_buffs()
            for buff in buffs :
                string_message += buff.get_name() + " "

        elif log[0] == CombatEventTypes.MOVE:
            string_message += log[1] + " moves from "
            string_message += str(log[2]) + " to " + str(log[3])

        elif log[0] == CombatEventTypes.ADD:
            string_message += log[1] + " appears at position " + str(log[2])

