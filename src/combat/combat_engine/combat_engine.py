from src.combat.combat_engine.combat_event_log import CombatEventLog
import functools
import random

"""
This class provides some basic functionality for combat logic
Has basic functionalities
Add unit : adds a unit to a given position
Remove unit : removes a unit with a given id
Use skill : asks a unit to use a skill on certain enemy
move unit : moves a unit to a new position

"""

class CombatEngine:
    def __init__(self):
        self.grid_x_length = 0
        self.grid_y_length = 0
        self.combat_units_dict = {}  # { unit id : combat unit object }
        self.grid_pos_dict = {}  # { grid pos : unit id }
        self.unit_pos_dict = {}  # { unit id : grid pos }
        self.unit_name_dict = {} # { unit id : unit name } this is for combat logging purposes
        self.combat_event_log = CombatEventLog()

    def reset(self, grid_x, grid_y):
        self.grid_x_length = grid_x
        self.grid_y_length = grid_y
        self.combat_units_dict = {}  # { unit id : combat unit object }
        self.grid_pos_dict = {}  # { grid_pos : unit id }

# ------------- first abstraction layer --------------
    def add_unit(self, unit_id, unit_name, unit, position):
        if self.check_position_occupied(position):
            return False
        if not self.check_valid_position(position):
            return False
        self.add_new_unit(unit, unit_id, position, unit_name)
        self.combat_event_log.log_add_unit_event(unit_name, position)
        return True

    def use_skill(self, using_unit_id, target_unit_position, skill):
        curr_active_combat_unit = self.get_combat_unit(using_unit_id)
        if not curr_active_combat_unit.is_alive():
            return False
        if not self.check_valid_position(target_unit_position):
            return False
        curr_active_combat_unit_name = self.get_unit_name_by_id(using_unit_id)
        target_combat_unit_id = self.get_unit_id_at_position(target_unit_position)
        target_combat_unit = self.get_combat_unit(target_combat_unit_id)
        target_combat_unit_name = self.get_combat_unit(target_combat_unit_id)
        damage_report = target_combat_unit.hit(skill)
        self.combat_event_log.log_use_skill_event(curr_active_combat_unit_name
                                                  , target_combat_unit_name, skill, damage_report)
        if not target_combat_unit.is_alive():
            self.combat_event_log.log_unit_death_event(target_combat_unit_name, target_unit_position)
        return True

    def move_unit(self, unit_id, new_position):
        curr_unit = self.get_combat_unit(unit_id)
        if not curr_unit.is_alive():
            return False
        if not self.check_valid_position(new_position) or self.check_position_occupied(new_position):
            return False
        curr_unit_name = self.get_unit_name_by_id(unit_id)
        curr_pos = self.get_combat_unit_position(unit_id)
        self.update_combat_unit_position(unit_id, new_position)
        self.combat_event_log.log_move_event(curr_unit_name, curr_pos, new_position)
        return True

    def tick_all_combat_units(self):
        for unit_id in self.combat_units_dict:
            self.combat_units_dict[unit_id].tick()

    def remove_combat_unit_with_id(self, unit_id):
        unit_pos = self.get_combat_unit_position(unit_id)
        self.combat_units_dict.pop(unit_id)
        self.unit_pos_dict.pop(unit_id)
        self.unit_name_dict.pop(unit_id)
        self.grid_pos_dict.pop(unit_pos)


# ----------- second abstraction layer -----------------
    def get_unit_name_by_id(self, combat_unit_id):
        return self.unit_name_dict[combat_unit_id]

    def get_combat_unit_by_position(self, position):
        unit_id = self.grid_pos_dict[position]
        return self.combat_units_dict[unit_id]

    def check_position_occupied(self, position):
        return position in self.grid_pos_dict

    # position is (x,y)
    def check_valid_position(self, position):
        return 0 <= position[0] <= self.grid_x_length and 0 <= position [1] <= self.grid_y_length

    def add_new_unit(self, new_combat_unit, new_unit_id, position, new_unit_name):
        self.grid_pos_dict[position] = new_unit_id
        self.unit_pos_dict[new_unit_id] = position
        self.combat_units_dict[new_unit_id] = new_combat_unit
        self.unit_name_dict[new_unit_id] = new_unit_name

    def get_combat_unit(self, unit_id):
        return self.combat_units_dict[unit_id]

    def get_unit_id_at_position(self, position):
        return self.grid_pos_dict[position]

    def get_combat_unit_position(self, unit_id):
        return self.unit_pos_dict[unit_id]

    def update_combat_unit_position(self, unit_id, new_position):
        old_position = self.unit_pos_dict[unit_id]
        self.grid_pos_dict.pop(old_position)
        self.grid_pos_dict[new_position] = unit_id
        self.unit_pos_dict[unit_id] = new_position


    # ------------ getters ---------------
    # gives the Game Master class all the access to the
    def get_combat_units_dict(self):
        return self.combat_units_dict

    def get_combat_log(self):
        return self.combat_event_log







