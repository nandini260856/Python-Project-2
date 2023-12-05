# Captain.py
from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")  # "V" is the symbol for the Captain
        self.__collected_veggies = []  # Private member variable for collected veggies

    # Method to add a Veggie to the Captain's collection
    def addVeggie(self, veggie):
        self.__collected_veggies.append(veggie)

    # Getter for collected_veggies
    def get_collected_veggies(self):
        return self.__collected_veggies

    # There's no need for a setter for collected_veggies as we don't replace the whole list,
    # but if you need to reset the list, you can use the following method
    def reset_collected_veggies(self):
        self.__collected_veggies = []
