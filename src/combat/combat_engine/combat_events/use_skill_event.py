from src.combat.combat_engine.combat_events.combat_event import CombatEvent
from src.combat.combat_engine.combat_events.combat_event_types import CombatEventTypes


class UseSkillEvent(CombatEvent):
    def __init__(self, targets, skill_num):
        super().__init__()
        self.event_type = CombatEventTypes.USE_SKILL
        self.targets = targets # the grid positions of the targets
        self.skill_num = skill_num

    def get_targets(self):
        return self.targets

    def get_skill_num(self):
        return self.skill_num

