from src.combat.combat_engine.combat_events.combat_event import CombatEvent
from src.combat.combat_engine.combat_events.combat_event_types import CombatEventTypes


class MoveEvent(CombatEvent):
    def __init__(self, move_vector):
        super().__init__()
        self.event_type = CombatEventTypes.MOVE
        self.move_vector = move_vector

    # move vector is (x,y)
    def get_move_vector(self):
        return self.move_vector
