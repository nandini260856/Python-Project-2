# Veggie.py
from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)  # Call to the superclass's constructor with symbol
        self.__name = name  # Private member variable
        self.__points = points  # Private member variable

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, value):
        self.__name = value

    # Getter for points
    def get_points(self):
        return self.__points

    # Setter for points
    def set_points(self, value):
        self.__points = value

    # Overridden __str__() function
    def __str__(self):
        return f"Symbol: {self._symbol}, Name: {self.__name}, Points: {self.__points}"
