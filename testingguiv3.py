
import random
import tkinter as tk
from PIL import Image, ImageTk

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

# Declare animation_label, message_label, sandwich_photo, and warning_photo as global variables
animation_label = None
message_label = None
sandwich_photo = None
warning_photo = None

# Function to load sandwich image
def load_sandwich_image():
    sandwich_img = Image.open("sandwich.png")
    sandwich_img = sandwich_img.resize((50, 50))  # Resize the image
    return ImageTk.PhotoImage(sandwich_img)

# Function to load warning image
def load_warning_image():
    warning_img = Image.open("warning.png")
    warning_img = warning_img.resize((50, 50))  # Resize the image
    return ImageTk.PhotoImage(warning_img)

# Function to handle finding items or encountering traps with animation
def handle_event_with_animation(stamina_points):
    global animation_label, message_label, sandwich_photo, warning_photo  # Access the global variables
    if random.random() <= 0.25:
        event = random.choice(["item", "trap"])
        if event == "item":
            if stamina_points > 80:
                stamina_points = min(stamina_points + 20, 100)
            elif stamina_points <= 80:
                print("You found a sandwich! You gained 20 stamina points!")
                stamina_points += 20

                # Show sandwich animation
                animation_label.config(image=sandwich_photo)
                message_label.config(text="You found a sandwich! You gained 20 stamina points!")
                root.update_idletasks()
                root.after(1500, lambda: animation_label.config(image=""))
                root.after(1500, lambda: message_label.config(text=""))
            elif stamina_points == 100:
                print("You found a sandwich but you weren't hungry and threw it away.")
        elif event == "trap":
            print("You encountered a trap! You lost 20 stamina points!")
            stamina_points -= 20
            if stamina_points <= 0:
                raise ValueError

            # Show warning animation
            animation_label.config(image=warning_photo)
            message_label.config(text="You encountered a trap! You lost 20 stamina points!")
            root.update_idletasks()
            root.after(1500, lambda: animation_label.config(image=""))
            root.after(1500, lambda: message_label.config(text=""))
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

    # Function to check if the new position is within the boundaries of the map
    def is_within_boundaries(row, col):
        return 0 <= row < 5 and 0 <= col < 5

    # Store the new row and column based on the user's choice
    new_row, new_col = current_row, current_column
    if choice == OPTIONS["Move up 1 square"]:
        new_row -= 1
    elif choice == OPTIONS["Move down 1 square"]:
        new_row += 1
    elif choice == OPTIONS["Move left 1 square"]:
        new_col -= 1
    elif choice == OPTIONS["Move right 1 square"]:
        new_col += 1

    # Check if the new position is within the boundaries
    if is_within_boundaries(new_row, new_col):
        current_row, current_column = new_row, new_col
        stamina_points = handle_event_with_animation(stamina_points)
    else:
        # Show the message if the new position is outside the map boundaries
        message_label.config(text="You can't move that way now, please pick a different direction.")
        root.update_idletasks()
        root.after(2000, lambda: message_label.config(text=""))

    update_gui()

# Function to print the introduction one sentence at a time with prompt for user input
def print_intro(index=0):
    global animation_label, sandwich_photo, warning_photo  # Access the global variables
    if index < len(INTRO):
        intro_label.config(text=INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_intro(i+1))  # Bind Enter key to proceed to the next sentence
    else:
        intro_label.config(text="")  # Clear the intro label after the introduction is over
        root.unbind("<Return>")  # Unbind the Enter key after the introduction is over

        # Create the animation label
        animation_label = tk.Label(root)
        animation_label.pack()

        # Create the message label
        global message_label
        message_label = tk.Label(root, wraplength=400)
        message_label.pack()

        # Load the sandwich and warning images
        global sandwich_photo, warning_photo
        sandwich_photo = load_sandwich_image()
        warning_photo = load_warning_image()

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
