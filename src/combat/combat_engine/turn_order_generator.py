import functools
import random


class TurnOrderGenerator:
    def __init__(self):
        self.turn_order_pointer = 0
        self.turn_order_size = 0
        self.threshold_speed = 100
        self.base_speed = 20
        self.curr_unit_id = None
        self.turn_order = []
        self.speed_roll_dict = {}
        self.speed_dict = {}

    def reset(self):
        self.turn_order_pointer = 0
        self.turn_order_size = 0
        self.threshold_speed = 100
        self.base_speed = 20
        self.curr_unit_id = None
        self.turn_order = []
        self.speed_roll_dict = {}
        self.speed_dict = {}

    def add_unit_speed(self, unit_id, speed):
        """ this stores the speed of the unit id which allows for turn order calculation """
        self.speed_dict[unit_id] = speed

    def generate_turn_order(self):
        """ generates a list of ids which represent the turn order and stores it into self.turn_order"""
        self.turn_order_pointer = 0
        self.speed_roll_dict = {}
        for unit_id in self.speed_dict:
            speed = self.speed_dict[unit_id]
            effective_speed = generate_effective_speed(speed, self.base_speed)
            self.speed_roll_dict[unit_id] = effective_speed
        speed_list = []
        for unit_id in self.speed_roll_dict:
            speed = self.speed_roll_dict[unit_id]
            while speed > self.threshold_speed:
                speed_list.append((unit_id, speed))
                speed = speed - self.threshold_speed
            speed_list.append((unit_id,speed))

        speed_list.sort(key = functools.cmp_to_key(compare_id_speed_tuple),reverse = True)
        self.turn_order = list(map( lambda x : x[0], speed_list))
        self.turn_order_size = len(self.turn_order)
        self.curr_unit_id = self.turn_order[self.turn_order_pointer]

    def has_next(self):
        """ is the current unit the last unit in the turn order """
        return self.turn_order_pointer >= self.turn_order_size

    def next_unit(self):
        """ sets the curr unit to the next unit in the turn order"""
        if not self.has_next():
            return None
        self.turn_order_pointer += 1



    def get_curr_unit_id(self):
        return self.curr_unit_id


def generate_effective_speed(speed, base_speed):
    return speed + random.randint(0, base_speed + speed)

    # tuple in the format : ( id, speed )
def compare_id_speed_tuple(tuple1, tuple2):
    speed1, speed2 = tuple1[1], tuple2[1]
    if speed1 > speed2:
        return 1
    elif speed1 < speed1:
        return 0
    else:
        return - 1

