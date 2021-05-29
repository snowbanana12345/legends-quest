"""
This class behaves as a struct class
{ key : value }
"""

class DataStruct:
    def __init__(self):
        self.dictionary = {}
        self.default_value = 0

    def set_data(self, data_key, data):
        self.dictionary[data_key] = data

    def get_data(self, data_key):
        if data_key not in self.dictionary:
            return self.default_value
        else :
            return self.dictionary[data_key]

    def get_dictionary(self):
        return self.dictionary

    def is_empty(self):
        return len(self.dictionary) == 0