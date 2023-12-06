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







