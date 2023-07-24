import random

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

# stamina_level
stamina_points = 100


# Function to handle finding items or encountering traps
def handle_event(stamina_points):
    if random.random() <= 0.1:
        event = random.choice(["item", "trap"])
        if event == "item":
            if stamina_points > 80:
                stamina_points = min(stamina_points + 20, 100) 
            elif stamina_points <= 80:
                print("You found a sandwich! You gained 20 stamina points!")
                stamina_points += 20
            elif stamina_points == 100:
                print("You found a sandwich but you weren't hungry and threw it away.")
        elif event == "trap":
            print("You encountered a trap! You lost 20 stamina points!")
            stamina_points -= 20
            if stamina_points <= 0:
                raise ValueError
    return stamina_points

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
try:
    user_choice = ""
    while True:
        print("You have {} stamina points.".format(stamina_points))
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

        while True:
            if user_choice == OPTIONS["Move up 1 square"]:
                if current_row > 0:
                    current_row -= 1
                    stamina_points = handle_event(stamina_points)
                    break
                else:
                    user_choice = check_validity(2, current_row, 0, user_choice, OPTIONS["Move up 1 square"])
            elif user_choice == OPTIONS["Move down 1 square"]:
                if current_row < 4:
                    current_row += 1
                    stamina_points = handle_event(stamina_points)
                    break 
                else:
                    user_choice = check_validity(2, current_row, 4, user_choice, OPTIONS["Move down 1 square"])
            elif user_choice == OPTIONS["Move left 1 square"]:
                if current_column > 0:
                    current_column -= 1
                    stamina_points = handle_event(stamina_points)
                    break
                else:
                    user_choice = check_validity(2, current_column, 0, user_choice, OPTIONS["Move left 1 square"])
            elif user_choice == OPTIONS["Move right 1 square"]:
                if current_column < 4:
                    current_column += 1
                    stamina_points = handle_event(stamina_points)
                    break
                else:
                    user_choice = check_validity(2, current_column, 4, user_choice, OPTIONS["Move right 1 square"])
            else:
                print("Invalid choice. Please try again.")
                user_choice = input("Please make a choice:")
                user_choice = user_choice.upper()

        # Reset user_choice to an empty string
        user_choice = ""
except ValueError:
    print("You've reach 0 stamina! You fainted, got sent home and could no longer continue in your search for Irene Indiana. Now, you'll never know the truth about what happened to her...GAME OVER")