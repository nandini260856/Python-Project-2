from GameEngine import GameEngine

def main():
    """
    The main function that runs the game.
    """
    # Instantiate a GameEngine object
    game_engine = GameEngine()

    # Initialize the game
    game_engine.initializeGame()

    # Display the game's introduction
    game_engine.intro()

    # Initialize the number of remaining vegetables in the game
    remaining_veggies = game_engine.remainingVeggies()

    # Game loop
    while remaining_veggies > 0:
        print(f"\nRemaining vegetables: {remaining_veggies}")
        print(f"Player's score: {game_engine.getScore()}")

        # Print out the field
        game_engine.printField()

        # Move the rabbits
        game_engine.moveRabbits()

        # Move the captain
        game_engine.moveCaptain()

        # Determine the new number of remaining vegetables
        remaining_veggies = game_engine.remainingVeggies()

    # Display the Game Over information
    game_engine.gameOver()

    # Handle the High Score functionality
    game_engine.highScore()

if __name__ == "__main__":
    main()
