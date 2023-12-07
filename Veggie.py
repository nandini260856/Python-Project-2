from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        """
        Initializes a Veggie object.

        :param name: The name of the veggie.
        :type name: str
        :param symbol: The symbol representing the veggie on the field.
        :type symbol: str
        :param points: The points value associated with the veggie.
        :type points: int
        """
        super().__init__(symbol)  # Call to the superclass's constructor with symbol
        self.__name = name  # Private member variable
        self.__points = points  # Private member variable

    def get_name(self):
        """
        Retrieves the name of the veggie.

        :return: The name of the veggie.
        :rtype: str
        """
        return self.__name

    def set_name(self, value):
        """
        Sets the name of the veggie.

        :param value: The new name value.
        :type value: str
        """
        self.__name = value

    def get_points(self):
        """
        Retrieves the points value associated with the veggie.

        :return: The points value.
        :rtype: int
        """
        return self.__points

    def set_points(self, value):
        """
        Sets the points value associated with the veggie.

        :param value: The new points value.
        :type value: int
        """
        self.__points = value

    def __str__(self):
        """
        Returns a string representation of the veggie.

        :return: A string containing veggie information.
        :rtype: str
        """
        return f"Symbol: {self._symbol}, Name: {self.__name}, Points: {self.__points}"
