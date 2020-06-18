from typing import List

class token():
    def __init__(self, function, variables: List):
        self.function = function
        self.variables = variables

    def __repr__(self):
        return str([self.function, self.variables])

    def __str__(self):
        s = "Function = " + str(self.function) + " - With variables(s): " + str(self.variables)
        return s

    def get_function(self):
        return self.function

    def get_variables(self):
        return self.variables

    def set_function(self, function):
        self.function = function

    def set_variables(self, variables: List):
        self.function = variables
