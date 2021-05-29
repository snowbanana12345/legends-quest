import functools
import random

from src.combat.combat_engine.combat_engine import CombatEngine
from src.combat.combat_engine.turn_order_generator import TurnOrderGenerator

"""
Turn ordering rules :
Each combat turn, a combat unit will have a effective speed = base speed + rolled speed
The rolled speed is uniformly between a minimum and a maximum
If the effective is higher than a certain treshold speed,
the combat unit gains another turn with effective speed = original effective speed - threshold speed

The game logic makes the following assumptions :
It is a turned based combat
The turn order is based on the combat unit's speed
Each turn, a combat unit can use a combat skill or move or pass its turn

Grid :
All combat units occupy grids , potentially some enemies occupy more than one grid
"""

class CombatMaster:
    def __init__(self):
        self.combat_engine = CombatEngine()
        self.turn_order_generator = TurnOrderGenerator()

    def generate_turn_order(self):
        self.turn_order_generator.reset()
        combat_unit_dict = self.combat_engine.get_combat_units_dict()
        for unit_id in combat_unit_dict:
            unit_speed = combat_unit_dict[unit_id]
            self.turn_order_generator.add_unit_speed(unit_id, unit_speed)
        self.turn_order_generator.generate_turn_order()

    



