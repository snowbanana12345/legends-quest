from src.combat.combat_engine.combat_engine import CombatEngine
from src.combat.combat_engine.turn_order_generator import TurnOrderGenerator
from src.combat.combat_engine.unit_id_generator import UnitIdGenerator

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
        self.unit_id_generator = UnitIdGenerator()

# ----------- initialization functions ----------------
    def generate_grid(self, grid_x, grid_y):
        self.combat_engine.reset(grid_x, grid_y)

    def generate_turn_order(self):
        self.turn_order_generator.reset()
        combat_unit_dict = self.combat_engine.get_combat_units_dict()
        for unit_id in combat_unit_dict:
            unit_speed = combat_unit_dict[unit_id]
            self.turn_order_generator.add_unit_speed(unit_id, unit_speed)
        self.turn_order_generator.generate_turn_order()

# ---------- combat logic functions ----------------
# returns True if the action is successfully executed, returns false other wise,
    # if false is returned, the state of the objects do not change

    def add_combat_unit(self, unit_name, unit_obj, position):
        new_unit_id = self.unit_id_generator.get_next_id()
        return self.combat_engine.add_unit(new_unit_id, unit_name, unit_obj, position)

    def end_turn(self):
        if self.turn_order_generator.has_next():
            self.turn_order_generator.next_unit()
        else :
            self.turn_order_generator.generate_turn_order()
        return True

    def use_skill(self, skill_num, target_position):
        using_unit_id = self.turn_order_generator.get_curr_unit_id()
        using_combat_unit = self.combat_engine.get_combat_unit(using_unit_id)

        # check if the unit has sufficient resources to use the skill
        is_skill_used = using_combat_unit.use_skill(skill_num)
        if not is_skill_used:
            return False

        self.combat_engine.use_skill(using_unit_id, target_position, skill_num)
        return True



