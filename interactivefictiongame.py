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
    "Good luck, brave student! Find Irene and save the school!"
]



# game menu
OPTIONS = {
    "Move up 1 square": "A",
    "Move down 1 square": "B",
    "Move left 1 square": "C",
    "Move right 1 square": "D",
}


current_row = 2  # starting row
current_column = 2  # starting column

# prints introduction

for sentence in INTRO:
    if sentence == INTRO[0]:
        print(sentence)
        input("*Press Enter to continue*\n")
    else:
        print(sentence)
        input()

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
