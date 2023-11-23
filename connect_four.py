while True:
    # Initialize the game here
    print("Initializing the game...")
    # Game code goes here
    # ...

    play_again = input("Play again? (y/n/r/q): ")
    if play_again.lower() == "n":
        quit()
    elif play_again.lower() == "y":
        # Restart the game by going back to the beginning of the loop
        continue
    elif play_again.lower() == "r":
        # Code to reset the game state goes here
        print("Resetting the game...")
        # Reset code goes here
        # ...
        continue
    elif play_again.lower() == "q":
        # Code to quit the game goes here
        print("Quitting the game...")
        quit()
    else:
        print("Invalid input. Please enter 'y', 'n', 'r', or 'q'.")
        continue
