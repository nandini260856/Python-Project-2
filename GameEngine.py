import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit



class GameEngine:
    """
    The main game engine for the Veggie Harvest Game.
    """
    __NUMBER_OF_VEGGIES = 30  # Private constant for initial number of vegetables
    __NUMBER_OF_RABBITS = 5   # Private constant for number of rabbits
    __HIGH_SCORE_FILE = "highscore.data"  # Private constant for the high score file name

    def __init__(self):
        """
        Initializes a GameEngine object.
        """
        self._field = []  # Member variable for the field (list)
        self._rabbits = []  # Member variable for the rabbits in the field (list)
        self._captain = None  # Member variable for the captain object
        self._veggies = []  # Member variable for all possible vegetables in the game (list)
        self._score = 0  # Member variable for the score

    def initVeggies(self):
        """
        Initializes the game field with vegetables based on a veggie file.
        """
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
        """
        Initializes the captain's position on the field.
        """
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
        """
        Initializes the positions of rabbits on the field.
        """
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
        """
        Initializes the game by setting up veggies, the captain, and rabbits on the field.
        """
         self.initVeggies()
         self.initCaptain()
         self.initRabbits()

    def remainingVeggies(self):
        """
        Counts the number of remaining vegetables on the field.

        :return: The number of remaining vegetables.
        :rtype: int
        """
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        """
        Displays the game's introduction.
        """
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
        """
        Prints the game field, including the symbols representing field inhabitants.
        """
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
        """
        Gets the player's score.

        :return: The player's score.
        :rtype: int
        """
        return self._score

    def moveRabbits(self):
        """
        Move the rabbits randomly within the field and handle interactions with other objects.

        Rabbits make random moves within the field. They will not move onto the Captain or other rabbits. If a rabbit
        moves onto a Veggie, it eats the Veggie.

        This method updates the positions of rabbits on the field.

        :return: None
        """
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
        """
        Move Captain Veggie vertically within the field and handle interactions with other objects.

        :param movement: The vertical movement direction (-1 for up, 1 for down).
        :type movement: int
        :return: None
        """
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
        """
    Move Captain Veggie horizontally within the field and handle interactions with other objects.

    :param movement: The horizontal movement direction (-1 for left, 1 for right).
    :type movement: int
    :return: None
    """
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


    def moveCaptain(self):
        """
    Move Captain Veggie based on user input and handle interactions within the game field.

    :return: None
    """
        direction = input("Which direction would you like to move Captain? (W, A, S, D): ").strip().lower()
        field_height = len(self._field)
        field_width = len(self._field[0]) if len(self._field) > 0 else 0

        if direction == "w":  # Move up
            if self._captain.get_x() > 0:
                self.moveCptVertical(-1)
            else:
                print("You cannot move that way.")
        elif direction == "s":  # Move down
            if self._captain.get_x() < field_height - 1:
                self.moveCptVertical(1)
            else:
                print("You cannot move that way.")
        elif direction == "a":  # Move left
            if self._captain.get_y() > 0:
                self.moveCptHorizontal(-1)
            else:
                print("You cannot move that way.")
        elif direction == "d":  # Move right
            if self._captain.get_y() < field_width - 1:
                self.moveCptHorizontal(1)
            else:
                print("You cannot move that way.")
        else:
            print("Invalid input. Please use W, A, S, or D.")

    def gameOver(self):
        """
    Display game over message and final score along with harvested vegetables.
    
    :return: None
    """
        print("Game Over!")
        print("Here are the vegetables Captain Veggie harvested:")

        for veggie in self._captain.get_collected_veggies():
            print(veggie.get_name())

        print(f"Your final score is: {self._score}")

    def highScore(self):
        """
    Handle the high score functionality, including displaying and updating high scores.

    :return: None
    """
        high_scores = []  # List to store high scores (initials, score)

        # Check if high score file exists and read from it
        if os.path.exists(GameEngine.__HIGH_SCORE_FILE):
            with open(GameEngine.__HIGH_SCORE_FILE, 'rb') as file:
                high_scores = pickle.load(file)

        # Prompt user for initials
        initials = input("Please enter your initials: ")[:3].upper()

        # Create tuple for current player's score
        player_score = (initials, self._score)

        # Add player's score to the high score list
        high_scores.append(player_score)
        high_scores.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order

        # Output high scores
        print("HIGH SCORES:")
        for score in high_scores:
            print(f"{score[0]}\t{score[1]}")

        # Write high scores back to file
        with open(GameEngine.__HIGH_SCORE_FILE, 'wb') as file:
            pickle.dump(high_scores, file)




