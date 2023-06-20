

# game menu
OPTIONS = {
    "Move up 1 square": "A",
    "Move down 1 square": "B",
    "Move left 1 square": "C",
    "Move right 1 square": "D",
}


current_row = 2  # starting row
current_column = 2  # starting column

# game loop
while True:
    print("\nMap of Onslow College. Your current position is marked with X.\n")
    # Display the board
    for row in range(5):
        for column in range(5):
            if row == current_row and column == current_column:
                # user's position
                print("X", end=" ")
            else:
                # empty cell
                print(".", end=" ")
        # newline after each row
        print()

    # Get user input for movement
    for option in OPTIONS:
        print("{}){}".format(OPTIONS[option], option))
    # asks the user to select an option from the main menu
    user_choice = input("Please make a choice:")
    user_choice = user_choice.upper()

    # Update user's position based on input
    if user_choice == OPTIONS["Move up 1 square"]:
        if current_row > 0:
            current_row -= 1
    elif user_choice == OPTIONS["Move down 1 square"]:
        if current_row < 4:
            current_row += 1
    elif user_choice == OPTIONS["Move left 1 square"]:
        if current_column > 0:
            current_column -= 1
    elif user_choice == OPTIONS["Move right 1 square"]:
        if current_column < 4:
            current_column += 1
    else:
        print("Invalid direction. Please try again.")
