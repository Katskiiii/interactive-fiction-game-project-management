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

# Global variable to track if the Art quiz is completed
art_quiz_completed = False

# Other variables
clue_label = None
move_count = 0


# Art quiz questions and answers
ART_QUIZ = [
    {
        "question": "Van Gogh famously cut off what part of his body?",
        "options": ["His ear", "His nose", "His finger", "His toe"],
        "answer": "His ear"
    },
    {
        "question": "What type of paint dries the slowest?",
        "options": ["Acrylic paint", "Watercolor", "Oil paint", "Gouache paint"],
        "answer": "Oil paint"
    },
    {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "options": ["Leonardo da Vinci", "Raphael", "Michelangelo", "Donatello"],
        "answer": "Michelangelo"
    }
]

# Function to handle the Art quiz
def art_quiz():
    global stamina_points, art_quiz_completed
    if not art_quiz_completed:
        quiz_score = 0
        for question_data in ART_QUIZ:
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["answer"]

            # Display the question and options on the message label
            message_label.config(text=question + "\n\n" + "\n".join(f"{i + 1}. {option}" for i, option in enumerate(options)))

            # Wait for the player's answer
            root.wait_variable(answer_var)

            # Check the answer
            if answer_var.get() == correct_answer:
                quiz_score += 1
            else:
                stamina_points -= 20
                message_label.config(text="Oh no you got a question wrong! Let's restart.")
                root.update_idletasks()
                root.after(2000, lambda: message_label.config(text=""))

                # Player needs to restart the quiz
                return

        if quiz_score == len(ART_QUIZ):
            # Player successfully completed the quiz
            art_quiz_completed = True
            message_label.config(text="Impressive! I didn't think a new student would know this much about art.\n"
                                      "Well, okay, here is Irene's last painting before she went missing.\n"
                                      "I hope it helps you to find her.")
            root.update_idletasks()
            root.after(4000, lambda: message_label.config(text=""))

            # Reveal the clue about Irene's favorite place
            clue_label.pack()
            root.update_idletasks()
            root.after(4000, lambda: clue_label.config(text="You place it down on a nearby desk. The painting seems to be an abstract perception of...beakers and tubes?\n"
                                                            "You notice written in the corner, is very small but neat writing. You look closer at it to see that it says \"my favourite place here...\".\n"
                                                            "You think that this can only mean one place. The science lab. You decide to head there next."))

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

# Function to update the GUI with the current game state
def update_gui():
    global current_row, current_column

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

    # Check if the player encounters the art studio
    if move_count == 2:
        # Remove the movement buttons and display Art Studio text
        for button in root.winfo_children():
            button.pack_forget()
        root.unbind("<Return>")  # Unbind Enter key

        # Display Art Studio text one sentence at a time
        art_studio_text = [
            "You come across the art studio. You decide to start your clue-finding journey here and go inside to hopefully talk to whoever is inside.",
            "Upon entering, the strong smell of paint and coffee hits you and a woman sitting at her desk looks up at you.",
            "\"A face I haven't seen before! I'm Ms. Kay, what brings you to my humble studio?\" A trill voice says.",
            "An eccentric-looking, paint-splattered face stares at yours as she walks up to you. Her hair is dishevelled and her glasses sit crooked on her face but she looks kind and welcoming somehow.",
            "You explain to her you are a new student and are looking for Irene.",
            "\"Ah...Irene. Such a shock. She was such an amazing student, it's so unlike her to disappear like this. Have you come here to look for her?\" Ms. Kay sighs.",
            "You ask if her she would have any idea on her whereabouts.",
            "\"Hmmm...I don't know where she could be...but I do know that she was in here all the time working on a new piece.",
            "It could be of some help, and I would let you see it but first I want to see if you're worthy! Get all the questions right in my quiz and I'll let you see Irene's latest painting.\""
        ]

        def show_next_sentence(index=0):
            if index < len(art_studio_text):
                message_label.config(text=art_studio_text[index])
                root.update_idletasks()
                root.after(3000, lambda: show_next_sentence(index + 1))
            else:
                # Start the Art quiz
                art_quiz()
                # Update the GUI after the quiz is completed
                update_gui()
        show_next_sentence()
    else:
        # Update the GUI in case the player didn't encounter the art studio
        root.update_idletasks()

# Function to handle user input from the GUI
def on_choice_button_click(choice):
    global current_row, current_column, stamina_points, move_count

    # Increment move count
    move_count += 1

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
        update_gui()  # Call update_gui() after the player's move
    else:
        # Show the message if the new position is outside the map boundaries
        message_label.config(text="You can't move that way now, please pick a different direction.")
        root.update_idletasks()
        root.after(2000, lambda: message_label.config(text=""))


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

# Create a variable to store the player's answer in the quiz
answer_var = tk.StringVar()

# Start the GUI event loop
root.mainloop()
