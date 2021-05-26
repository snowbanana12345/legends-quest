from src.combat.combat_engine.combat_events.combat_event import CombatEvent


class AddUnitEvent(CombatEvent):
    def __init__(self, combat_unit, position, unit_id, name):
        super().__init__()
        self.combat_unit = combat_unit
        self.position = position
        self.unit_id = unit_id
        self.name = name

    def get_new_unit_name(self):
        return self.name

    def get_new_unit_position(self):
        return self.position

    def get_combat_unit(self):
        return self.combat_unit

    def get_unit_id(self):
        return self.unit_id