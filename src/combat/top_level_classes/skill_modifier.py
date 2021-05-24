import copy
"""
Abstract class SkillModifier
All it holds is a method that modifies an old skill and returns a new skill
it contains potentially other parameters

"""
class SkillModifier:
    def __init__(self):
        pass

    """
    This method MUST return a reference to a new skill object
    DO NOT modify the input skill object
    DO NOT ever modify skill objects
    """
    def modify_skill(self, old_skill):
        return copy.copy(old_skill)

