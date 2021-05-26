from src.combat.combat_engine.combat_events.add_unit_event import AddUnitEvent
from src.combat.combat_engine.combat_engine import CombatEngine
from src.combat.combat_engine.combat_events.combat_start_event import CombatStartEvent
from src.combat.combat_engine.combat_events.end_turn_event import EndTurnEvent
from src.combat.combat_engine.combat_events.use_skill_event import UseSkillEvent
from src.combat.combat_engine.test_hero import Noob
from src.combat.enemy.undead.zombie import Zombie

combat_engine = CombatEngine()
combat_engine.reset(10, 10)

noob = Noob()
zombie = Zombie()

events = []
events.append(AddUnitEvent(noob, (5,5), 1, "Noob in underwear"))
events.append(AddUnitEvent(zombie, (5,4), 2, "Dummy Zombie"))
events.append(CombatStartEvent())
for i in range(10):
    events.append(UseSkillEvent([(5,4)], 1))
    events.append(EndTurnEvent())
    events.append(UseSkillEvent([(5,5)], 1))
    events.append(EndTurnEvent())

for event in events:
    combat_engine.accept_event(event)

for log in combat_engine.combat_event_log.event_log:
    print(combat_engine.combat_event_log.event_to_string_message(log))
