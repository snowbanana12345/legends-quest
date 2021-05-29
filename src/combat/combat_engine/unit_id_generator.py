class UnitIdGenerator:
    def __init__(self):
        self.curr_value = 0
        self.base_value = 0

    def reset(self):
        self.curr_value = self.base_value

    def get_next_id(self):
        self.curr_value += 1
        return self.curr_value

