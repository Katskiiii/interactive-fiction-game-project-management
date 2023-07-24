import random
import tkinter as tk

# Introduction of game
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

# Game menu
OPTIONS = {
    "Move up 1 square": "A",
    "Move down 1 square": "B",
    "Move left 1 square": "C",
    "Move right 1 square": "D",
}

# Current position
current_row = 2  # starting row
current_column = 2  # starting column

# Stamina level
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

# Function to update the GUI with the current game state
def update_gui():
    map_text = ""
    for row in range(5):
        for col in range(5):
            if row == current_row and col == current_column:
                map_text += "X "
            else:
                map_text += ". "
        map_text += "\n"
    map_label.config(text=map_text)

    stamina_label.config(text="Stamina: {}".format(stamina_points))

# Function to handle user input from the GUI
def on_choice_button_click(choice):
    global current_row, current_column, stamina_points
    if choice == OPTIONS["Move up 1 square"]:
        if current_row > 0:
            current_row -= 1
            stamina_points = handle_event(stamina_points)
    elif choice == OPTIONS["Move down 1 square"]:
        if current_row < 4:
            current_row += 1
            stamina_points = handle_event(stamina_points)
    elif choice == OPTIONS["Move left 1 square"]:
        if current_column > 0:
            current_column -= 1
            stamina_points = handle_event(stamina_points)
    elif choice == OPTIONS["Move right 1 square"]:
        if current_column < 4:
            current_column += 1
            stamina_points = handle_event(stamina_points)
    update_gui()

# Function to print the introduction one sentence at a time with prompt for user input
def print_intro(index=0):
    if index < len(INTRO):
        intro_label.config(text=INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_intro(i+1))  # Bind Enter key to proceed to the next sentence
    else:
        intro_label.config(text="")  # Clear the intro label after the introduction is over
        for option, choice in OPTIONS.items():
            button = tk.Button(root, text=option, command=lambda choice=choice: on_choice_button_click(choice))
            button.pack()
        update_gui()  # Show the map, stamina counter, and controls

# Create the main window
root = tk.Tk()
root.title("Where in Onslow College is Irene Indiana")

# Create and place GUI elements
intro_label = tk.Label(root, text="", wraplength=400)
intro_label.pack()

map_label = tk.Label(root, font=("Courier New", 20))
map_label.pack()

stamina_label = tk.Label(root, text="Stamina: {}".format(stamina_points))
stamina_label.pack()

# Start printing the introduction
print_intro()

# Start the GUI event loop
root.mainloop()
