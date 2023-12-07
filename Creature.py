from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        Initializes a Creature object.

        :param x: The x-coordinate of the Creature's position.
        :type x: int
        :param y: The y-coordinate of the Creature's position.
        :type y: int
        :param symbol: The symbol representing the Creature on the field.
        :type symbol: str
        """
        super().__init__(symbol)  # Call to the superclass's constructor with symbol
        self._x = x  # Protected member variable for x coordinate
        self._y = y  # Protected member variable for y coordinate

    def get_x(self):
        """
        Retrieves the x-coordinate of the Creature.

        :return: The x-coordinate.
        """
        return self._x

    def set_x(self, value):
        """
        Sets the x-coordinate of the Creature.

        :param value: The new x-coordinate value.
        :type value: int
        """
        self._x = value

    def get_y(self):
        """
        Retrieves the y-coordinate of the Creature.

        :return: The y-coordinate.
        """
        return self._y

    def set_y(self, value):
        """
        Sets the y-coordinate of the Creature.

        :param value: The new y-coordinate value.
        :type value: int
        """
        self._y = value
