# Rabbit.py
from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")  # "R" is the symbol for the Rabbit

    # If there are additional attributes or methods specific to the Rabbit they can be added here

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
