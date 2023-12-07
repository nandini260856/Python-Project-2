from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        Initializes a Rabbit object.

        :param x: The x-coordinate of the Rabbit's position.
        :type x: int
        :param y: The y-coordinate of the Rabbit's position.
        :type y: int
        """
        super().__init__(x, y, "R")  # "R" is the symbol for the Rabbit

    # If there are additional attributes or methods specific to the Rabbit, they can be added here

    def get_x(self):
        """
        Retrieves the x-coordinate of the Rabbit.

        :return: The x-coordinate.
        :rtype: int
        """
        return self._x

    def set_x(self, value):
        """
        Sets the x-coordinate of the Rabbit.

        :param value: The new x-coordinate value.
        :type value: int
        """
        self._x = value

    def get_y(self):
        """
        Retrieves the y-coordinate of the Rabbit.

        :return: The y-coordinate.
        :rtype: int
        """
        return self._y

    def set_y(self, value):
        """
        Sets the y-coordinate of the Rabbit.

        :param value: The new y-coordinate value.
        :type value: int
        """
        self._y = value
