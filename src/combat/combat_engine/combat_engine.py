from src.combat.combat_engine.combat_engine_states import CombatEngineStates
from src.combat.combat_engine.combat_event_types import CombatEventTypes
import functools
import random

"""
The responsibility of the combat engine is to store the current state of the combat
Combat logic is handled mostly outside the scope of this class, including checking if a skill can even be used
This class is only responsible for the execution of the combat logic, it doesn't even care if a unit is a hero or an enemy


The game logic makes the following assumptions :
It is a turned based combat
The turn order is based on the combat unit's speed
Each turn, a combat unit can use a combat skill or move or pass its turn

Grid :
All combat units occupy grids , potentially some enemies occupy more than one grid

Turn ordering rules :
Each combat turn, a combat unit will have a effective speed = base speed + rolled speed
The rolled speed is uniformly between a minimum and a maximum
If the effective is higher than a certain treshold speed,
the combat unit gains another turn with effective speed = original effective speed - threshold speed
"""


def get_new_position(curr_position, move_vector):
    return (curr_position[0] + move_vector[0], curr_position[1] + move_vector[1])

def generate_effective_speed(speed, base_speed):
    return speed + random.randint(0, base_speed + speed)

# tuple in the format : ( id, speed )
def compare_id_speed_tuple(tuple1, tuple2):
    speed1, speed2 = tuple1[1], tuple2[1]
    if speed1 > speed2 :
        return 1
    elif speed1 < speed1 :
        return 0
    else :
        return - 1


class CombatEngine:
    def __init__(self):
        self.grid_x_length = 0
        self.grid_y_length = 0
        self.combat_units_dict = {}  # { unit id : combat unit object }
        self.grid_pos_dict = {}  # { grid pos : unit id }
        self.unit_pos_dict = {}  # { unit id : grid pos }
        self.speed_roll_dict = {}  # { unit id : speed roll }
        self.turn_order = None  # iterator which keeps generating the id of the combat unit which gets to move next
        self.turn_order_pointer = 0
        self.turn_order_size = 0
        self.threshold_speed = 100
        self.base_speed = 20
        self.unit_id = 1
        self.last_used_id = 1
        self.engine_state = CombatEngineStates.INITIAL
        self.active_combat_unit_id = None

    def reset(self, grid_x, grid_y):
        self.grid_x_length = grid_x
        self.grid_y_length = grid_y
        self.combat_units_dict = {}  # { unit id : combat unit object }
        self.grid_pos_dict = {}  # { grid_pos : unit id }
        self.speed_roll_dict = {}  # { unit id : speed roll }
        self.turn_order = None  # sorted list of unit ids, units that get multiple turns can have their id repeated
        self.engine_state = CombatEngineStates.INITIAL
        self.reset_id()
        self.active_combat_unit_id = None

    """
    Takes in a event to change the game engine state
    returns True if the event is accepted and the engine incorperates the event
    return False if the event is rejected and nothing happens
    """
    def accept_event(self, combat_event):
        event_type = combat_event.get_event_type()
        if event_type == CombatEventTypes.ADD: # new combat units can be added during TURN as well
            if self.engine_state == CombatEngineStates.END:
                return False
            new_combat_unit = combat_event.get_combat_unit()
            position = combat_event.get_new_unit_position()
            if self.check_position_occupied(position):
                return False
            if not self.check_valid_position(position):
                return False
            new_unit_id = self.next_id()
            self.add_new_unit(new_combat_unit, new_unit_id, position)
            return True

        elif event_type == CombatEventTypes.USE_SKILL: # skills can only be used during the combat turn
            if not self.engine_state == CombatEngineStates.TURN:
                return False
            curr_active_combat_unit = self.get_combat_unit(self.active_combat_unit_id)
            if not curr_active_combat_unit.is_alive():
                return False
            skill_num = combat_event.get_skill_num()
            if not curr_active_combat_unit.has_skill(skill_num):
                return False
            skill = curr_active_combat_unit.get_skill(skill_num)
            skill_used = curr_active_combat_unit.use_skill(skill_num)
            if not skill_used:
                return False
            target_positions = combat_event.get_targets()
            targets_hit = 0
            for position in target_positions:
                if not self.check_valid_position(position):
                    continue
                if not self.check_position_occupied(position):
                    continue
                target_combat_unit = self.get_combat_unit_at_position(position)
                if not target_combat_unit.is_alive():
                    continue
                target_combat_unit.hit(skill)
                targets_hit = targets_hit + 1
            if targets_hit == 0:
                return False
            return True

        elif event_type == CombatEventTypes.MOVE:
            if self.engine_state == CombatEngineStates.END:
                return False
            curr_active_combat_unit = self.get_combat_unit(self.active_combat_unit_id)
            if not curr_active_combat_unit.is_alive():
                return False
            move_vec = combat_event.get_move_vec()
            curr_position = self.get_combat_unit_position(self.active_combat_unit_id)
            new_position = get_new_position(curr_position, move_vec)
            if not self.check_valid_position(new_position) or self.check_position_occupied(new_position):
                return False
            self.update_combat_unit_position(self.active_combat_unit_id, new_position)
            return True

        elif event_type == CombatEventTypes.END_TURN:
            if not self.engine_state == CombatEngineStates.TURN:
                return False
            next_unit_id = self.get_next_combat_unit_id()
            if not next_unit_id : # end turn event is sent when the last unit finished it turn
                self.regenerate_turn_order() # restart the entire combat turn cycle
                self.tick_all_combat_units() # update the buff/debuff durations of all combat units
            else :
                self.active_combat_unit_id = next_unit_id

    def reset_id(self):
        self.last_used_id = 1
        self.unit_id = 1

    def next_id(self):
        self.last_used_id = self.unit_id
        self.unit_id = self.unit_id + 1
        return self.unit_id

    def get_last_used_id(self):
        return self.last_used_id

    def check_position_occupied(self, position):
        return position in self.grid_pos_dict

    # position is (x,y)
    def check_valid_position(self, position):
        return 0 <= position[0] <= self.grid_x_length and 0 <= position [1] <= self.grid_y_length

    def add_new_unit(self, new_combat_unit, new_unit_id, position):
        self.grid_pos_dict[position] = new_unit_id
        self.unit_pos_dict[new_unit_id] = position
        self.combat_units_dict[new_unit_id] = new_combat_unit

    def get_combat_unit(self, unit_id):
        return self.combat_units_dict[unit_id]

    def get_combat_unit_at_position(self, position):
        return self.grid_pos_dict[position]

    def get_combat_unit_position(self, unit_id):
        return self.unit_pos_dict[unit_id]

    def update_combat_unit_position(self, unit_id, new_position):
        old_position = self.unit_pos_dict[unit_id]
        self.grid_pos_dict.pop(old_position)
        self.grid_pos_dict[new_position] = unit_id
        self.unit_pos_dict[unit_id] = new_position

    def regenerate_turn_order(self):
        self.turn_order_pointer = 0
        self.speed_roll_dict = {}
        for unit_id in self.combat_units_dict:
            combat_unit = self.combat_units_dict[unit_id]
            speed = combat_unit.get_speed()
            effective_speed = generate_effective_speed(speed, self.base_speed)
            self.speed_roll_dict[unit_id] = effective_speed
        speed_list = []
        for unit_id in self.speed_roll_dict:
            speed = self.speed_roll_dict[unit_id]
            while speed > self.threshold_speed:
                speed_list.append((unit_id, speed))
                speed = speed - self.threshold_speed
            speed_list.append(speed)

        speed_list.sort(key = functools.cmp_to_key(compare_id_speed_tuple),reverse = True)
        self.turn_order = list(map( lambda x : x[0], speed_list))
        self.turn_order_size = len(self.turn_order)

        self.active_combat_unit_id = self.turn_order[self.turn_order_pointer]

    # returns the next id if it exists, returns None if all the combat units have used up their turn
    def get_next_combat_unit_id(self):
        self.turn_order_pointer = self.turn_order_pointer + 1
        if self.turn_order_pointer >= self.turn_order_size:
            return None
        return self.turn_order[self.turn_order_pointer]

    def tick_all_combat_units(self):
        for unit_id in self.combat_units_dict:
            self.combat_units_dict[unit_id].tick()




