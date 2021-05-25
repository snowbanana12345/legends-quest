from src.combat.combat_engine.combat_event import CombatEvent


class AddUnitEvent(CombatEvent):
    def __init__(self, combat_unit, position):
        super().__init__()
        self.combat_unit = combat_unit
        self.position = position

    def get_new_unit_position(self):
        return self.position

    def get_combat_unit(self):
        return self.combat_unit