"""
Abstract class for combat events

"""

class CombatEvent:
    def __init__(self):
        self.event_type = None

    def get_event_type(self):
        return self.event_type