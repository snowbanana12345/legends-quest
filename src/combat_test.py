from src.combat.combat_engine.combat_engine import CombatEngine
from src.combat.combat_engine.test_hero import Noob
from src.combat.enemy.undead.zombie import Zombie

combat_engine = CombatEngine()
combat_engine.reset(10, 10)

noob = Noob()
zombie = Zombie()




for log in combat_engine.combat_event_log.event_log:
    print(combat_engine.combat_event_log.event_to_string_message(log))
