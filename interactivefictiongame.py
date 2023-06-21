# introduction of game
INTRO = [
    "Welcome to 'Where in Onslow College is Irene Indiana'.",
    "You are a new student at Onslow College eager to learn, however, another student, 'Indiana Irene' has gone missing.",
    "Everyone is worried about her, and school cannot resume unless she is found.",
    "Your courageous self has taken the task to solve the mystery of her disappearance.",
    "Around Onslow are teachers who you can talk with to collect clues, but, they won’t give up their information for free.",
    "Complete their quizzes to find new clues that will lead you closer and closer to the truth.",
    "But beware! Someone has set up booby traps around the school to prevent you from finding Irene.",
    "These will diminish your stamina but don’t worry because you can also find food or other items around the school that will refill your stamina.",
    "Stamina will also be essential for completing the teachers' quizzes.",
    "Make sure that you always have some stamina because once your stamina runs out, you’ll be sent home and won’t be able to continue your investigation.",
    "Good luck, brave student! Find Irene and save school!"
]


# game menu
OPTIONS = {
    "Move up 1 square": "A",
    "Move down 1 square": "B",
    "Move left 1 square": "C",
    "Move right 1 square": "D",
}

# current position
current_row = 2  # starting row
current_column = 2  # starting column

# function to check input validity
def check_validity(invalid_1_or_2, column_or_row, max_row_or_column, user_choice, option):
    if invalid_1_or_2 == 1:
        while user_choice not in OPTIONS.values():
            print("Invalid direction. Please try again.")
            user_choice = input("Please make a choice:")
            user_choice = user_choice.upper()
    elif invalid_1_or_2 == 2:
        while column_or_row == max_row_or_column and user_choice == option:
            print("You cannot move that way.")
            user_choice = input("Please make a choice:")
            user_choice = user_choice.upper()
            if user_choice not in OPTIONS.values():
                user_choice = check_validity(1, current_column, 0, user_choice, OPTIONS["Move down 1 square"])
    return user_choice

# prints introduction
for sentence in INTRO:
    if sentence == INTRO[0]:
        print(sentence)
        input("*Press Enter to continue*\n")
    else:
        print(sentence)
        input()

# game loop
user_choice = ""
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
    
    if user_choice not in OPTIONS.values():
        user_choice = check_validity(1, current_column, 0, user_choice, OPTIONS["Move down 1 square"])

    # Update user's position based on input
    if user_choice == OPTIONS["Move up 1 square"]:
        if current_row > 0:
            current_row -= 1
        elif current_row == 0:
            user_choice = check_validity(2, current_row, 0, user_choice, OPTIONS["Move up 1 square"])
    if user_choice == OPTIONS["Move down 1 square"]:
        if current_row < 4:
            current_row += 1
        elif current_row == 4:
            user_choice = check_validity(2, current_row, 4, user_choice, OPTIONS["Move down 1 square"])
    if user_choice == OPTIONS["Move left 1 square"]:
        if current_column > 0:
            current_column -= 1
        elif current_column == 0:
            user_choice = check_validity(2, current_column, 0, user_choice, OPTIONS["Move left 1 square"])
    if user_choice == OPTIONS["Move right 1 square"]:
        if current_column < 4:
            current_column += 1
        elif current_column == 4:
            user_choice = check_validity(2, current_column, 4, user_choice, OPTIONS["Move right 1 square"])
    user_choice = ""