class FieldInhabitant:
    def __init__(self, symbol):
        """
        Initializes a FieldInhabitant object.

        :param symbol: The symbol representing the inhabitant on the field.
        :type symbol: str
        """
        self._symbol = symbol  # Protected member variable

    def get_symbol(self):
        """
        Retrieves the symbol representing the FieldInhabitant.

        :return: The symbol.
        :rtype: str
        """
        return self._symbol

    def set_symbol(self, value):
        """
        Sets the symbol representing the FieldInhabitant.

        :param value: The new symbol value.
        :type value: str
        """
        self._symbol = value
