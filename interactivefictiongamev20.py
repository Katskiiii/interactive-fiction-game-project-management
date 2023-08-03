import random
import tkinter as tk
from PIL import Image, ImageTk

# Additional text for the math classroom and Mr. Smith's introduction
MATH_CLASSROOM_INTRO = [
    "After finding the math classroom, you walk straight in. What must be the math teacher stands in front of a blackboard with chalk in his hand and a deep, thoughtful expression on his face as he looks at the math equations on the board.",
    "You clear your voice to get his attention, feeling bad that you’re interrupting his work. \"Oh! I’m sorry, I didn’t even notice someone came in. You must be the new student the principal told me about. I’m Mr. Smith.\"",
    "You shake his hand and introduce yourself. Once again you explain to him everything to do with Irene’s disappearance. You show him the equation written in Irene’s diary.",
    "\"Hmm...well, this is quite a complicated problem, but I think I can solve it. The principal said that I should help you catch up with the rest of the class when school starts again, so let me test you on some math, and I’ll solve that problem for you.\"",
    "Mr. Smith takes out a piece of paper and writes down some questions for you."
]

# Additional text after the math quiz is completed
AFTER_MATH_QUIZ_TEXT = [
    "\"Wow! Looks like I don’t have much stuff to catch you up on. Alright, give me a second to let me solve Irene’s equation.\"",
    "After a few minutes, Mr. Smith hands you back a slip of paper with the answer written on it. '2735' it says.",
    "You thank him and immediately start looking for the abandoned hallway. It feels like you’re so close to finding Irene...",
]

MATH_QUIZ_QUESTIONS = [
    {
        "question": "What is the formula for the circumference of a circle?",
        "options": ["1/2bh", "a^2 + b^2 = c^2", "2πr", "d/r"],
        "correct_answer": "2πr"
    },
    {
        "question": "What is 1/3 x 1/2?",
        "options": ["2/6", "2/3", "3/8", "1/6"],
        "correct_answer": "1/6"
    },
    {
        "question": "What is the hypotenuse?",
        "options": ["Side opposite right angle in a right triangle", "Biggest angle in a triangle ", "Shortest side of any triangle", "Side adjacent a right angle in a triangle"],
        "correct_answer": "Side opposite right angle in a right triangle"
    }
]

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

SCIENCE_LAB_INTRO = [
    "You finally find the science lab and walk inside. Hunched over a desk with a plethora of different coloured liquids and pieces of equipment is a strange man wearing safety glasses and a white lab coat.",
    "You walk up to him and ask if he’s the science teacher. \"Why yes, I am. I don’t think I’ve ever seen you in class before...I’m Mr. Green, pleased to meet you. What can I do for you?\"",
    "You introduce yourself as the new student looking for Irene. You tell him of Irene’s painting and ask him if he knew anything that could explain why Irene’s favourite place was the science lab.",
    "His face goes 2 shades paler... \"I’ll show you a secret...but only if you get 100% on my science quiz...\""
]

# Additional text after the science quiz is completed
AFTER_SCIENCE_QUIZ_TEXT = [
    "\"Wow, you really know your stuff! As promised, here's the secret I'll share with you...\"",
    "Mr. Green opens a drawer and pulls out a small diary, handing it to you. \"This is Irene's personal diary that she left behind with her disappearance. She often wrote her thoughts and feelings in here. Maybe it will provide some insight into her disappearance.\"",
    "You thank Mr. Green for his help, and open up the diary to read it.",
    "You find many long, boring recounts of Irene's day over the past week. However, on the last page you find what seems to be a very complex math equation.",
    "The page is titled 'abondoned hallway room'.",
    "A code to a secret room...You think to yourself.",
    "Unable to figure out the answer to the equation on your own, you decide to go to the math classroom to seek help with solving it"
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

# List of science quiz questions and their possible answers
SCIENCE_QUIZ_QUESTIONS = [
    {
        "question": "Where are the smallest bones in our body located?",
        "options": ["Hands", "Feet", "Spine", "Ear"],
        "correct_answer": "Ear"
    },
    {
        "question": "What organelle does photosynthesis occur in?",
        "options": ["Chloroplast", "Nucleus", "Mitochondria", "Golgi body"],
        "correct_answer": "Chloroplast"
    },
    {
        "question": "What is the most abundant gas in our atmosphere?",
        "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Argon"],
        "correct_answer": "Nitrogen"
    }
]

# Additional text for the secret room
SECRET_ROOM_INTRO = [
    "Your investigation leads you to a hidden door in the abandoned hallway. The door is padlocked, and curiosity takes over as you wonder what could be inside.",
    "You recall the code from Irene's equation - '2735'. Hesitant yet determined, you enter the code, and the padlock clicks open.",
    "As the door creaks open, you find yourself facing a flight of stairs that lead down to a dark basement. The air is heavy with a sense of mystery, and your heart races as you cautiously descend into the unknown depths.",
    "The faint sound of distant voices grows louder with each step, filling you with anticipation and apprehension.",
    "As you reach the bottom of the stairs, you find yourself in a dimly lit chamber filled with shadows.",
    "To your shock, you discover a secret society gathering led by the evil and mad history teacher, Mr. Scrooge. Amongst the crowd, you catch a glimpse of Irene.",
    "\"Help me please! He’s insane!\" Irene pleads for your help.",
    "Facing the sinister Mr. Scrooge, you demand to know why he took Irene.",
    "With a wicked grin, he says \"I don’t know who you are, but neither you nor Irene will stop me from achieving my goals. You want to know what Irene did to get herself here? I’ll tell you. She was too curious for her own good, she should have never discovered us, and she certainly should not have tried to stop us.",
    "You too will suffer the same fate as her...Unless! If you can complete my history quiz, one that no one has ever managed to conquer, then I will set you and Irene free.",
    "Your mind races with thoughts. It is a life-or-death wager. If you succeed, you and Irene shall be set free, but if you fail, you'll share Irene's fate in the cell.",
    "You tell him you’ll do it."
]

# Additional text after the secret room quiz is completed
AFTER_SECRET_ROOM_QUIZ_TEXT = [
    "The room falls silent as you complete the final question, leaving Mr. Scrooge no choice but to admit defeat.",
    "Defeated, Mr. Scrooge allows you and Irene to go free. The secret society members are apprehended, and their sinister ambitions are thwarted.",
    "Irene, freed from her confinement, embraces you with heartfelt gratitude, thanking you for being her savior.",
    "With the secret society exposed and Mr. Scrooge brought to justice, the school can once again resume its normal operations.",
    "You are hailed as a hero, celebrated for your bravery and ingenuity in saving Irene and the entire school from impending doom.",
    "As the days go by, you and Irene become the talk of the school, and your friendship grows stronger with each passing moment.",
    "The echoes of your courageous journey will forever resonate in the halls of Onslow, reminding everyone that even in the face of darkness, knowledge and bravery will always prevail."
]

# Secret room quiz questions
SECRET_ROOM_QUIZ_QUESTIONS = [
    {
        "question": "When did World War II end?",
        "options": ["1944", "1945", "1950", "1939"],
        "correct_answer": "1945"
    },
    {
        "question": "Who is the ‘father’ of western philosophy?",
        "options": ["Plato", "Socrates", "Aristotle", "Heraclitus"],
        "correct_answer": "Socrates"
    },
    {
        "question": "What is considered the largest empire in history?",
        "options": ["Roman Empire", "British Empire", "Mongol Empire", "Ottoman Empire"],
        "correct_answer": "British Empire"
    }
]

# Global variable to track if the secret room intro has been shown
secret_room_intro_shown = False

# Declare a set to store the visited positions on the board
visited_positions = set()

# Current position
current_row = 2  # starting row
current_column = 2  # starting column

# Stamina level
stamina_points = 100

# Global variable to track the player's move count
move_count = 0

# Variable to keep track of quiz attempts
quiz_attempts = 0

# Global variable to track if the science lab intro has been shown
science_lab_intro_shown = False

# Declare animation_label, message_label, sandwich_photo, and warning_photo as global variables
animation_label = None
message_label = None
sandwich_photo = None
warning_photo = None

# Global variable to track if the player has visited the art studio
visited_art_studio = False

# Global variable to track if the science lab intro has been shown
science_lab_intro_shown = False


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
    global current_row, current_column, stamina_points, visited_art_studio, move_count, visited_positions, science_lab_intro_shown, secret_room_intro_shown

    # Function to check if the new position is within the boundaries of the map
    def is_within_boundaries(row, col):
        return 0 <= row < 5 and 0 <= col < 5

    # Check if there is text being displayed or if a quiz window is open
    if intro_label.cget("text") or 'quiz_window' in globals():
        # Player cannot move when text is being displayed or during a quiz
        return

    # Check if the player's new position is a previously visited position
    new_row, new_col = current_row, current_column
    if choice == OPTIONS["Move up 1 square"]:
        new_row -= 1
    elif choice == OPTIONS["Move down 1 square"]:
        new_row += 1
    elif choice == OPTIONS["Move left 1 square"]:
        new_col -= 1
    elif choice == OPTIONS["Move right 1 square"]:
        new_col += 1

    new_position = (new_row, new_col)

    # Check if the new position is within the boundaries
    if is_within_boundaries(new_row, new_col):
        if new_position not in visited_positions:
            visited_positions.add(new_position)  # Add the new position to the set of visited positions
            move_count += 1  # Increment the move count each time the player makes a move

        # Check if the player has taken their 3rd move and trigger the art studio intro
        if move_count == 3 and not visited_art_studio:
            visited_art_studio = True  # Set the flag to True after the art studio introduction is shown
            print_art_studio_intro()
        if move_count == 5 and not visited_art_studio and not science_lab_intro_shown:
            visited_art_studio = True  # Set the flag to True after the art studio introduction is shown
            print_art_studio_intro()
        elif move_count == 6 and not science_lab_intro_shown:
            print_science_lab_intro()  # Show the science lab intro directly on the 6th move
        elif move_count == 8 and not math_classroom_intro_shown:
            print_math_classroom_intro()  # Show the math classroom intro directly on the 8th move
        elif move_count == 11 and not secret_room_intro_shown:
            print_secret_room_intro()
        else:
            current_row, current_column = new_row, new_col
            stamina_points = handle_event_with_animation(stamina_points)
    else:
        # Show the message if the new position is outside the map boundaries
        message_label.config(text="You can't move that way now, please pick a different direction.")
        root.update_idletasks()
        root.after(2000, lambda: message_label.config(text=""))

    update_gui()

def print_math_classroom_intro(index=0):
    global math_classroom_intro_shown  # Access the global variable

    if index < len(MATH_CLASSROOM_INTRO):
        intro_label.config(text=MATH_CLASSROOM_INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_math_classroom_intro(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Directly handle the math quiz once the math classroom intro is over
        handle_math_quiz()

        # Update the flag to indicate that the math classroom intro has been shown
        math_classroom_intro_shown = True

        update_gui()
    
math_classroom_intro_shown = False

# Function to handle the math quiz
def handle_math_quiz():
    global stamina_points, message_label, button_frame, game_state, stamina_label

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Math Quiz")

    # Function to check the quiz answers
    def check_math_answers():
        global quiz_attempts, stamina_points, message_label, stamina_label

        # Get the selected answer for each question
        selected_answers = [var.get() for var in math_answer_vars]

        # Check if all answers are correct
        if all(selected_answer == question["correct_answer"] for selected_answer, question in zip(selected_answers, MATH_QUIZ_QUESTIONS)):
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            quiz_window.destroy()  # Close the quiz window

            # Display the "Wow! Looks like I don’t have much stuff to catch you up on." message above the board one sentence at a time
            print_after_math_quiz_text()
        else:
            # Player got a question wrong, deduct 20 stamina points and ask to retry
            stamina_points -= 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="Oh no you got a question wrong! You lost 20 stamina. Let's restart")
            root.update_idletasks()
            root.after(2000, lambda: message_label.config(text=""))
            # Clear the selected answers
            for var in math_answer_vars:
                var.set(None)


    # Create answer variables for each math quiz question
    math_answer_vars = [tk.StringVar() for _ in MATH_QUIZ_QUESTIONS]

    # Create math quiz questions and answer options
    for index, question in enumerate(MATH_QUIZ_QUESTIONS):
        math_question_frame = tk.Frame(quiz_window)
        math_question_frame.pack(pady=10)

        tk.Label(math_question_frame, text=question["question"]).pack()

        # Create answer options
        for option in question["options"]:
            tk.Radiobutton(math_question_frame, text=option, variable=math_answer_vars[index], value=option).pack(anchor="w")

    # Create a button to check answers
    check_math_button = tk.Button(quiz_window, text="Check Answers", command=check_math_answers)
    check_math_button.pack(pady=10)

    # Update the game state to "math_quiz" while the math quiz is displayed
    game_state = "math_quiz"


def print_after_math_quiz_text(index=0):
    if index < len(AFTER_MATH_QUIZ_TEXT):
        intro_label.config(text=AFTER_MATH_QUIZ_TEXT[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_after_math_quiz_text(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        update_gui()



# Function to handle the science quiz
def handle_science_quiz():
    global stamina_points, message_label, button_frame, game_state, stamina_label

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Science Quiz")

    # Function to check the quiz answers
    def check_science_answers():
        global quiz_attempts, stamina_points, message_label, stamina_label

        # Get the selected answer for each question
        selected_answers = [var.get() for var in science_answer_vars]

        # Check if all answers are correct
        if all(selected_answer == question["correct_answer"] for selected_answer, question in zip(selected_answers, SCIENCE_QUIZ_QUESTIONS)):
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            quiz_window.destroy()  # Close the quiz window

            # Display the "Wow, you really know your stuff!" message above the board one sentence at a time
            print_after_science_quiz_text()
        else:
            # Player got a question wrong, deduct 20 stamina points and ask to retry
            stamina_points -= 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="Oh no you got a question wrong! You lost 20 stamina. Let's restart")
            root.update_idletasks()
            root.after(2000, lambda: message_label.config(text=""))
            # Clear the selected answers
            for var in science_answer_vars:
                var.set(None)

    # Create answer variables for each science quiz question
    science_answer_vars = [tk.StringVar() for _ in SCIENCE_QUIZ_QUESTIONS]

    # Create science quiz questions and answer options
    for index, question in enumerate(SCIENCE_QUIZ_QUESTIONS):
        science_question_frame = tk.Frame(quiz_window)
        science_question_frame.pack(pady=10)

        tk.Label(science_question_frame, text=question["question"]).pack()

        # Create answer options
        for option in question["options"]:
            tk.Radiobutton(science_question_frame, text=option, variable=science_answer_vars[index], value=option).pack(anchor="w")

    # Create a button to check answers
    check_science_button = tk.Button(quiz_window, text="Check Answers", command=check_science_answers)
    check_science_button.pack(pady=10)

    # Update the game state to "science_quiz" while the science quiz is displayed
    game_state = "science_quiz"

def print_after_science_quiz_text(index=0):
    if index < len(AFTER_SCIENCE_QUIZ_TEXT):
        intro_label.config(text=AFTER_SCIENCE_QUIZ_TEXT[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_after_science_quiz_text(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        update_gui()


# Function to print the science lab introduction one sentence at a time with prompt for user input
def print_science_lab_intro(index=0):
    global science_lab_intro_shown  # Access the global variable

    if index < len(SCIENCE_LAB_INTRO):
        intro_label.config(text=SCIENCE_LAB_INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_science_lab_intro(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Directly handle the science quiz once the science lab intro is over
        handle_science_quiz()

        # Update the flag to indicate that the science lab intro has been shown
        science_lab_intro_shown = True

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
def handle_event_with_animation(stamina_points, show_animation=True):
    global animation_label, message_label, sandwich_photo, warning_photo  # Access the global variables

    # If show_animation is False, then no animation will be shown
    if not show_animation:
        return stamina_points
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
    if index < len(ART_STUDIO_INTRO):
        intro_label.config(text=ART_STUDIO_INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_art_studio_intro(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Directly handle the quiz once the art studio intro is over
        handle_quiz()

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
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
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

        update_gui()

# Function to print the secret room introduction one sentence at a time with prompt for user input
def print_secret_room_intro(index=0):
    global secret_room_intro_shown  # Access the global variable

    if index < len(SECRET_ROOM_INTRO):
        intro_label.config(text=SECRET_ROOM_INTRO[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_secret_room_intro(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Directly handle the secret room quiz once the secret room intro is over
        handle_secret_room_quiz()

        # Update the flag to indicate that the secret room intro has been shown
        secret_room_intro_shown = True

        update_gui()


# Function to handle the secret room quiz
def handle_secret_room_quiz():
    global stamina_points, message_label, button_frame, game_state, stamina_label

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Secret Room Quiz")

    # Function to check the quiz answers
    def check_secret_room_answers():
        global quiz_attempts, stamina_points, message_label, stamina_label

        # Get the selected answer for each question
        selected_answers = [var.get() for var in secret_room_answer_vars]

        # Check if all answers are correct
        if all(selected_answer == question["correct_answer"] for selected_answer, question in zip(selected_answers, SECRET_ROOM_QUIZ_QUESTIONS)):
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            quiz_window.destroy()  # Close the quiz window

            # Display the "\"Incredible! You have solved the riddles and proved yourself worthy to uncover the secret of this room.\"" message above the board one sentence at a time
            print_after_secret_room_quiz_text()
        else:
            # Player got a question wrong, deduct 20 stamina points and ask to retry
            stamina_points -= 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="Oh no you got a question wrong! You lost 20 stamina. Let's restart")
            root.update_idletasks()
            root.after(2000, lambda: message_label.config(text=""))
            # Clear the selected answers
            for var in secret_room_answer_vars:
                var.set(None)

    # Create answer variables for each secret room quiz question
    secret_room_answer_vars = [tk.StringVar() for _ in SECRET_ROOM_QUIZ_QUESTIONS]

    # Create secret room quiz questions and answer options
    for index, question in enumerate(SECRET_ROOM_QUIZ_QUESTIONS):
        secret_room_question_frame = tk.Frame(quiz_window)
        secret_room_question_frame.pack(pady=10)

        tk.Label(secret_room_question_frame, text=question["question"]).pack()

        # Create answer options
        for option in question["options"]:
            tk.Radiobutton(secret_room_question_frame, text=option, variable=secret_room_answer_vars[index], value=option).pack(anchor="w")

    # Create a button to check answers
    check_secret_room_button = tk.Button(quiz_window, text="Check Answers", command=check_secret_room_answers)
    check_secret_room_button.pack(pady=10)

    # Update the game state to "secret_room_quiz" while the secret room quiz is displayed
    game_state = "secret_room_quiz"


def print_after_secret_room_quiz_text(index=0):
    if index < len(AFTER_SECRET_ROOM_QUIZ_TEXT):
        intro_label.config(text=AFTER_SECRET_ROOM_QUIZ_TEXT[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_after_secret_room_quiz_text(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

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

