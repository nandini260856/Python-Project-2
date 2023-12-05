# Creature.py
from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)  # Call to the superclass's constructor with symbol
        self._x = x  # Protected member variable for x coordinate
        self._y = y  # Protected member variable for y coordinate

    # Getter for x coordinate
    def get_x(self):
        return self._x

    # Setter for x coordinate
    def set_x(self, value):
        self._x = value

    # Getter for y coordinate
    def get_y(self):
        return self._y

    # Setter for y coordinate
    def set_y(self, value):
        self._y = value
