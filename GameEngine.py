# GameEngine.py
import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit



class GameEngine:
    __NUMBER_OF_VEGGIES = 30  # Private constant for initial number of vegetables
    __NUMBER_OF_RABBITS = 5   # Private constant for number of rabbits
    __HIGH_SCORE_FILE = "highscore.data"  # Private constant for the high score file name

    def __init__(self):
        self._field = []  # Member variable for the field (list)
        self._rabbits = []  # Member variable for the rabbits in the field (list)
        self._captain = None  # Member variable for the captain object
        self._veggies = []  # Member variable for all possible vegetables in the game (list)
        self._score = 0  # Member variable for the score

    def initVeggies(self):
        # Prompting for the veggie file
        while True:
            file_name = input("Enter the name of the veggie file: ")
            if os.path.exists(file_name):
                break
            else:
                print("File not found. Please try again.")

        with open(file_name, 'r') as file:
            # Read the first line and split it
            first_line = file.readline().strip().split(',')

            # Skip the first element ('Field') and convert the remaining elements to integers
            field_size = tuple(map(int, first_line[1:3]))

            self._field = [[None for _ in range(field_size[1])] for _ in range(field_size[0])]

            # Create Veggie objects
            for line in file:
                name, symbol, points = line.strip().split(',')
                self._veggies.append(Veggie(name, symbol, int(points)))

        # Populate the field with veggies
        for _ in range(GameEngine.__NUMBER_OF_VEGGIES):
            while True:
                x, y = random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1)
                if self._field[x][y] is None:
                    self._field[x][y] = random.choice(self._veggies)
                    break


     
    def initCaptain(self):
        field_height = len(self._field)
        field_width = len(self._field[0]) if field_height > 0 else 0

        # Randomly choose a location for the Captain
        while True:
            x, y = random.randint(0, field_height - 1), random.randint(0, field_width - 1)
            if self._field[x][y] is None:
                # Create a new Captain object and place it on the field
                self._captain = Captain(x, y)
                self._field[x][y] = self._captain
                break

    def initRabbits(self):
        field_height = len(self._field)
        field_width = len(self._field[0]) if field_height > 0 else 0

        for _ in range(GameEngine.__NUMBER_OF_RABBITS):
            while True:
                x, y = random.randint(0, field_height - 1), random.randint(0, field_width - 1)
                if self._field[x][y] is None:
                    # Create a new Rabbit object and place it on the field
                    rabbit = Rabbit(x, y)
                    self._rabbits.append(rabbit)
                    self._field[x][y] = rabbit
                    break

    def initializeGame(self):
         self.initVeggies()
         self.initCaptain()
         self.initRabbits()

    def remainingVeggies(self):
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        print("Welcome to the Veggie Harvest Game!")
        print("In this game, you'll help Captain Veggie to harvest as many vegetables as possible.")
        print("Beware of the rabbits, as they are also trying to get the veggies!")
        print("\nHere are the vegetables you can find in the field:")

        for veggie in self._veggies:
            print(veggie)  # Using the __str__ method of Veggie class for printing

        print("\nIn this adventure, 'V' represents Captain Veggie and 'R' represents the rabbits.")
        print("Your goal is to navigate the field, harvest veggies, and avoid rabbits.")
        print("Good luck and have fun!")


    def printField(self):
        print("################################")  # Top border
        for row in self._field:
            print("# ", end="")
            for item in row:
                if item is None:
                    print("  ", end="")  # Empty space
                else:
                    print(item.get_symbol() + " ", end="")  # Symbol of the field inhabitant
            print("#")  # End of row border
        print("################################")  # Bottom border

    def getScore(self):
        return self._score

    def moveRabbits(self):
        field_height = len(self._field)
        field_width = len(self._field[0]) if field_height > 0 else 0

        for rabbit in self._rabbits:
            dx, dy = random.randint(-1, 1), random.randint(-1, 1)  # Random move direction
            new_x, new_y = rabbit.get_x() + dx, rabbit.get_y() + dy

            # Check for field boundaries
            if 0 <= new_x < field_height and 0 <= new_y < field_width:
                # Check for other Rabbit or Captain
                if not isinstance(self._field[new_x][new_y], Rabbit) and self._field[new_x][new_y] != self._captain:
                    # Move Rabbit and update previous location to None
                    self._field[rabbit.get_x()][rabbit.get_y()] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)

                    # Check and handle if Rabbit moves onto a Veggie
                    if isinstance(self._field[new_x][new_y], Veggie):
                        # Rabbit eats the Veggie
                        self._field[new_x][new_y] = rabbit


    def moveCptVertical(self, movement):
        field_height = len(self._field)
        new_x = self._captain.get_x() + movement

        # Check for field boundaries
        if 0 <= new_x < field_height:
            target = self._field[new_x][self._captain.get_y()]
            # Check for empty slot or Veggie
            if target is None or isinstance(target, Veggie):
                # Move Captain and update previous location to None
                old_x = self._captain.get_x()
                self._field[old_x][self._captain.get_y()] = None
                self._captain.set_x(new_x)

                if isinstance(target, Veggie):
                    # Output message, add Veggie to Captain's list, and update score
                    print(f"Yummy! A delicious {target.get_name()} found.")
                    self._captain.addVeggie(target)
                    self._score += target.get_points()

                # Assign the Captain to the new location
                self._field[new_x][self._captain.get_y()] = self._captain

            # Check for Rabbit
            elif isinstance(target, Rabbit):
                print("Oops! You should not step on the rabbits.")

    def moveCptHorizontal(self, movement):
        field_width = len(self._field[0]) if len(self._field) > 0 else 0
        new_y = self._captain.get_y() + movement

        # Check for field boundaries
        if 0 <= new_y < field_width:
            target = self._field[self._captain.get_x()][new_y]
            # Check for empty slot or Veggie
            if target is None or isinstance(target, Veggie):
                # Move Captain and update previous location to None
                old_y = self._captain.get_y()
                self._field[self._captain.get_x()][old_y] = None
                self._captain.set_y(new_y)

                if isinstance(target, Veggie):
                    # Output message, add Veggie to Captain's list, and update score
                    print(f"Yummy! A delicious {target.get_name()} found.")
                    self._captain.addVeggie(target)
                    self._score += target.get_points()

                # Assign the Captain to the new location
                self._field[self._captain.get_x()][new_y] = self._captain

            # Check for Rabbit
            elif isinstance(target, Rabbit):
                print("Oops! You should not step on the rabbits.")

   



