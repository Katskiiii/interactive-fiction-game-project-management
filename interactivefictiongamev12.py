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

# Additional text for the art studio and Ms. Kay's introduction
ART_STUDIO_INTRO = [
    "You come across the art studio. You decide to start your clue-finding journey here and go inside to hopefully talk to whoever is inside.",
    "Upon entering, the strong smell of paint and coffee hits you and a woman sitting at her desk looks up at you.",
    "\"A face I haven't seen before! I'm Ms. Kay, what brings you to my humble studio?\" A trill voice says.",
    "An eccentric-looking, paint-splattered face stares at yours as she walks up to you. Her hair is disheveled and her glasses sit crooked on her face but she looks kind and welcoming somehow.",
    "You explain to her you are a new student and are looking for Irene. \"Ah...Irene. Such a shock. She was such an amazing student, it's so unlike her to disappear like this. Have you come here to look for her?\" Ms. Kay sighs.",
    "You ask if she would have any idea about her whereabouts. \"Hmmm...I don't know where she could be...but I do know that she was in here all the time working on a new piece.",
    "It could be of some help, and I would let you see it but first I want to see if you're worthy! Get all the questions right in my quiz and I'll let you see Irene's latest painting.\""
]

# Game menu
OPTIONS = {
    "Move up 1 square": "A",
    "Move down 1 square": "B",
    "Move left 1 square": "C",
    "Move right 1 square": "D",
}

# Additional text after the quiz is completed
AFTER_QUIZ_TEXT = [
    "\"Impressive! I didn't think a new student would know this much about art. Well, okay, here is Irene's last painting before she went missing.\" Ms. Kay hands over a large canvas.",
    "You place it down on a nearby desk. The painting seems to be an abstract perception of...beakers and tubes?",
    "You notice written in the corner, is very small but neat writing. You look closer at it to see that it says \"my favourite place here...\".",
    "You think that this can only mean one place. The science lab. You decide to head there next."
]

# List of quiz questions and their possible answers
QUIZ_QUESTIONS = [
    {
        "question": "Van Gogh famously cut off what part of his body?",
        "options": ["Ear", "Nose", "Finger", "Toe"],
        "correct_answer": "Ear"
    },
    {
        "question": "What type of paint dries the slowest?",
        "options": ["Acrylic", "Oil", "Watercolor", "Gouache"],
        "correct_answer": "Oil"
    },
    {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
        "correct_answer": "Michelangelo"
    }
]


# Current position
current_row = 2  # starting row
current_column = 2  # starting column

# Stamina level
stamina_points = 100

# Global variable to track the player's move count
move_count = 0

# Variable to keep track of quiz attempts
quiz_attempts = 0

# Declare animation_label, message_label, sandwich_photo, and warning_photo as global variables
animation_label = None
message_label = None
sandwich_photo = None
warning_photo = None

# Global variable to track if the player has visited the art studio
visited_art_studio = False

# Global variable to track the game state
game_state = "intro"  # Possible values: "intro", "art_studio_intro", "quiz", "gameplay"

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

    # Disable the movement buttons during the art studio intro
    for widget in button_frame.winfo_children():
        widget["state"] = "normal" if game_state == "gameplay" else "disabled"


# Function to handle user input from the GUI
def on_choice_button_click(choice):
    global current_row, current_column, stamina_points, visited_art_studio, move_count, game_state

    # Function to check if the new position is within the boundaries of the map
    def is_within_boundaries(row, col):
        return 0 <= row < 5 and 0 <= col < 5

    # Check if the buttons should be active based on the game state
    if game_state != "gameplay":
        return

    move_count += 1  # Increment the move count each time the player makes a move

    # Check if the player has taken their second move and show the art studio introduction
    if move_count == 2 and not visited_art_studio:
        visited_art_studio = True  # Set the flag to True after the art studio introduction is shown
        print_art_studio_intro()
        return

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
                stamina_points += 20

                # Show sandwich animation
                animation_label.config(image=sandwich_photo)
                message_label.config(text="You found a sandwich! You ate it and gained 20 stamina points!")
                root.update_idletasks()
                root.after(1500, lambda: animation_label.config(image=""))
                root.after(1500, lambda: message_label.config(text=""))
            elif stamina_points == 100:
                print("You found a sandwich but you weren't hungry and threw it away.")
        elif event == "trap":
            stamina_points -= 20

            # Show warning animation
            animation_label.config(image=warning_photo)
            message_label.config(text="You encountered a trap! You tripped and lost 20 stamina points!")
            root.update_idletasks()
            root.after(1500, lambda: animation_label.config(image=""))
            root.after(1500, lambda: message_label.config(text=""))
    return stamina_points


# Function to print the introduction one sentence at a time with prompt for user input
def print_intro(index=0):
    global animation_label, sandwich_photo, warning_photo, game_state  # Access the global variables
    if index < len(INTRO):
        intro_label.config(text=INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_intro(i + 1))  # Bind Enter key to proceed to the next sentence
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

        # Update the game state to "gameplay" after the introduction is over
        game_state = "gameplay"

        update_gui()  # Show the map, stamina counter, and controls


# Declare button_frame as a global variable
button_frame = None

# Function to print the art studio introduction one sentence at a time with prompt for user input
def print_art_studio_intro(index=0):
    global game_state, button_frame
    if index < len(ART_STUDIO_INTRO):
        intro_label.config(text=ART_STUDIO_INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_art_studio_intro(i + 1))

        # Update the game state to "art_studio_intro" while the art studio intro is displayed
        game_state = "art_studio_intro"

        # Disable the movement buttons during the art studio intro
        for widget in button_frame.winfo_children():
            widget["state"] = "disabled"

    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the introduction is over

        # Directly handle the quiz once the art studio intro is over
        handle_quiz()

        # Re-enable the movement buttons after the art studio intro is over
        for widget in button_frame.winfo_children():
            widget["state"] = "normal"

        update_gui()
    
# Function to handle the quiz
def handle_quiz():
    global stamina_points, message_label, button_frame, game_state, stamina_label

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Art Quiz")

    # Function to check the quiz answers
    def check_answers():
        global quiz_attempts, stamina_points, message_label, stamina_label

        # Get the selected answer for each question
        selected_answers = [var.get() for var in answer_vars]

        # Check if all answers are correct
        if all(selected_answer == question["correct_answer"] for selected_answer, question in zip(selected_answers, QUIZ_QUESTIONS)):
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points)  # Show the animation and update stamina
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            quiz_window.destroy()  # Close the quiz window

            # Display the "Impressive!" message above the board one sentence at a time
            print_after_quiz_text()
        else:
            # Player got a question wrong, deduct 20 stamina points and ask to retry
            stamina_points -= 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="Oh no you got a question wrong! You lost 20 stamina. Let's restart")
            root.update_idletasks()
            root.after(2000, lambda: message_label.config(text=""))
            # Clear the selected answers
            for var in answer_vars:
                var.set(None)


    # Create answer variables for each question
    answer_vars = [tk.StringVar() for _ in QUIZ_QUESTIONS]

    # Create quiz questions and answer options
    for index, question in enumerate(QUIZ_QUESTIONS):
        question_frame = tk.Frame(quiz_window)
        question_frame.pack(pady=10)

        tk.Label(question_frame, text=question["question"]).pack()

        # Create answer options
        for option in question["options"]:
            tk.Radiobutton(question_frame, text=option, variable=answer_vars[index], value=option).pack(anchor="w")

    # Create a button to check answers
    check_button = tk.Button(quiz_window, text="Check Answers", command=check_answers)
    check_button.pack(pady=10)

    # Update the game state to "quiz" while the quiz is displayed
    game_state = "quiz"

def print_after_quiz_text(index=0):
    if index < len(AFTER_QUIZ_TEXT):
        intro_label.config(text=AFTER_QUIZ_TEXT[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_after_quiz_text(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Directly handle the movement to the science lab after the quiz text is over
        handle_movement_to_science_lab()

        update_gui()

# Function to handle the movement to the science lab after the quiz text is displayed
def handle_movement_to_science_lab():
    global game_state

    # Set the player's position to the science lab (assumed position)
    current_row = 3
    current_column = 2

    # Update the game state to "gameplay" for movement after the quiz text is displayed
    game_state = "gameplay"

    update_gui()

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