from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        """
        Initializes a Captain object.
        
        :param x: The x-coordinate of the Captain's position.
        :type x: int
        :param y: The y-coordinate of the Captain's position.
        :type y: int
        """
        super().__init__(x, y, "V")  # "V" is the symbol for the Captain
        self.__collected_veggies = []  # Private member variable for collected veggies

    def addVeggie(self, veggie):
        """
        Adds a Veggie to the Captain's collection.

        :param veggie: The Veggie to be added to the collection.
        :type veggie: Veggie
        """
        self.__collected_veggies.append(veggie)

    def get_collected_veggies(self):
        """
        Retrieves the list of collected veggies by the Captain.
        :return: A list of collected veggies.
        """
        return self.__collected_veggies

    def reset_collected_veggies(self):
        """
        Resets the list of collected veggies to an empty list.
        """
        self.__collected_veggies = []
