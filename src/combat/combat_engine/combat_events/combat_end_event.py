from src.combat.combat_engine.combat_events.combat_event import CombatEvent
from src.combat.combat_engine.combat_events.combat_event_types import CombatEventTypes


class CombatEndEvent(CombatEvent):
    def __init__(self):
        super().__init__()
        self.event_type = CombatEventTypes.END
