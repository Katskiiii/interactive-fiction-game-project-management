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
    "You are a new student at Onslow College eager to learn, however, another student, 'Indiana Irene' has gone missing. Everyone is worried about her, and school cannot resume unless she is found.",
    "Your courageous self has taken the task to solve the mystery of her disappearance. Around Onslow are teachers who you can talk with to collect clues, but, they won’t give up their information for free.",
    "Complete their quizzes to find new clues that will lead you closer and closer to the truth. But beware! Someone has set up booby traps around the school to prevent you from finding Irene.",
    "These will diminish your stamina but don’t worry because you can also find food or other items around the school that will refill your stamina.",
    "Stamina will also be essential for completing the teachers' quizzes. Make sure that you always have some stamina because once your stamina runs out, you’ll be sent home and won’t be able to continue your investigation.",
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
    "With a wicked grin, he says \"I don’t know who you are, but neither you nor Irene will stop me from achieving my goals. \"My plan is take over this entire school and then I shall finally be the most powerful teacher here again.",
    "You want to know what Irene did to get herself here? I’ll tell you. She was too curious for her own good, she should have never discovered us, and she certainly should not have tried to stop us.",
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
        "question": "How did Julius Caesar die",
        "options": ["Stabbed", "Drowned", "Strangled", "Shot"],
        "correct_answer": "Stabbed"
    },
    {
        "question": "When did the first iphone come out?",
        "options": ["2009", "2000", "1998", "2007"],
        "correct_answer": "2007"
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
                map_text += "옷 "
            else:
                map_text += ". "
        map_text += "\n"
    map_label.config(text=map_text)

    stamina_label.config(text="Stamina: {}".format(stamina_points))

    # Enable or disable the movement buttons based on the game state
    button_state = "normal" if game_state == "gameplay" else "disabled"
    for widget in button_frame.winfo_children():
        widget["state"] = button_state
    

# Function to handle user input from the GUI
def on_choice_button_click(choice):
    global current_row, current_column, stamina_points, visited_art_studio, move_count, visited_positions, science_lab_intro_shown, secret_room_intro_shown, game_state

    message_label.config(text="")
    root.update_idletasks()
    
    # Check if there is text being displayed or if a quiz window is open
    if intro_label.cget("text") or 'quiz_window' in globals():
        # Player cannot move when text is being displayed or during a quiz
        display_cannot_move_message()
        return

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
        if move_count == 6 and not science_lab_intro_shown:
            print_science_lab_intro()  # Show the science lab intro directly on the 6th move
        if move_count == 7 and not science_lab_intro_shown:
            print_science_lab_intro()
        if move_count == 8 and not math_classroom_intro_shown:
            print_math_classroom_intro()  # Show the math classroom intro directly on the 8th move
        if move_count == 9 and not math_classroom_intro_shown:
            print_math_classroom_intro()
        if move_count == 11 and not secret_room_intro_shown:
            print_secret_room_intro()
        if move_count == 12 and not secret_room_intro_shown:
            print_secret_room_intro()
        else:
            current_row, current_column = new_row, new_col
            stamina_points = handle_event_with_animation(stamina_points)
    else:
        # Show the message if the new position is outside the map boundaries
        message_label.config(text="You can't move that way now, please pick a different direction.",fg = "red")
        root.update_idletasks()
        root.after(2000, lambda: message_label.config(text=""))

        # Check if the player's stamina reaches 0
    if stamina_points <= 0:
        handle_stamina_zero()
    else:
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

    # Prompt the player to answer the questions
    tk.Label(quiz_window, text="Answer these math questions to continue:").pack()

    # List to store question labels to reference later
    question_labels = []

    # Function to check the quiz answers
    def check_math_answers():
        nonlocal question_labels  # Access the local variable in the outer scope

        global quiz_attempts, stamina_points, message_label, stamina_label, game_state

        # Get the selected answer for each question
        selected_answers = [var.get() for var in math_answer_vars]

        # List to store incorrect question indices
        incorrect_questions = []

        # Check if any question is left unanswered
        unanswered_questions = [i+1 for i, selected_answer in enumerate(selected_answers) if not selected_answer]
        if unanswered_questions:
            message_label.config(text="Please answer questions {} and try again.".format(", ".join(map(str, unanswered_questions))), fg="red")
            return

        # Check if all answers are correct
        for index, (selected_answer, question) in enumerate(zip(selected_answers, MATH_QUIZ_QUESTIONS)):
            if selected_answer != question["correct_answer"]:
                incorrect_questions.append(index)
        
        # Update the message label to show which question(s) were incorrect and deduct 20 stamina points
        if incorrect_questions:
            stamina_points -= 10
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label

            incorrect_question_text = "Question(s) {} are incorrect. You lost 10 stamina points.".format(
                ", ".join(str(i+1) for i in incorrect_questions))

            message_label.config(text=incorrect_question_text, fg = "red")
            root.update_idletasks()

            if stamina_points <= 0:
                handle_stamina_zero()
        else:
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_points += 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="You completed the quiz and got 20 stamina!", fg = "green")
            root.after(2000, lambda: message_label.config(text=""))

            # Disable the "Check Answers" button after the quiz is completed
            check_math_button.config(state="disabled")

            # Destroy the quiz window after a delay
            quiz_window.destroy()

            # Display the "You're a math whiz!" message above the board one sentence at a time
            print_after_math_quiz_text()



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
        enable_arrow_key()



# Function to handle the science quiz
def handle_science_quiz():
    global stamina_points, message_label, button_frame, game_state, stamina_label

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Science Quiz")

    # Prompt the player to answer the questions
    tk.Label(quiz_window, text="Answer these science to continue questions:").pack()

    # List to store question labels to reference later
    question_labels = []

    # Function to check the quiz answers
    def check_science_answers():
        nonlocal question_labels  # Access the local variable in the outer scope

        global quiz_attempts, stamina_points, message_label, stamina_label, game_state

        # Get the selected answer for each question
        selected_answers = [var.get() for var in science_answer_vars]

        # List to store incorrect question indices
        incorrect_questions = []

        # Check if any question is left unanswered
        unanswered_questions = [i+1 for i, selected_answer in enumerate(selected_answers) if not selected_answer]
        if unanswered_questions:
            message_label.config(text="Please answer questions {} and try again.".format(", ".join(map(str, unanswered_questions))), fg="red")
            return


        # Check if all answers are correct
        for index, (selected_answer, question) in enumerate(zip(selected_answers, SCIENCE_QUIZ_QUESTIONS)):
            if selected_answer != question["correct_answer"]:
                incorrect_questions.append(index)
        
        # Update the message label to show which question(s) were incorrect and deduct 20 stamina points
        if incorrect_questions:
            stamina_points -= 10
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label

            incorrect_question_text = "Question(s) {} are incorrect. You lost 10 stamina points.".format(
                ", ".join(str(i+1) for i in incorrect_questions))

            message_label.config(text=incorrect_question_text, fg = "red")
            root.update_idletasks()

            if stamina_points <= 0:
                handle_stamina_zero()
        else:
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_points += 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="You completed the quiz and got 20 stamina!", fg = "green")
            root.after(2000, lambda: message_label.config(text=""))

            quiz_window.destroy()

            print_after_science_quiz_text()

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
        enable_arrow_key()


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

# Variable to keep track of location found count
location_found_count = 0

# Function to handle finding items or encountering traps with animation
def handle_event_with_animation(stamina_points, show_animation=True):
    global animation_label, message_label, sandwich_photo, warning_photo, location_found_count  # Access the global variables

    # If show_animation is False, then no animation will be shown
    if not show_animation:
        return stamina_points

    # Check if the location should trigger an event
    if move_count in [3, 6, 9, 13]:
        location_found_count += 1
    else:
        if random.random() <= 0.25:
            event = random.choice(["item", "trap"])
            if event == "item":
                stamina_points += 20
                # Show sandwich animation
                animation_label.config(image=sandwich_photo)
                message_label.config(text="You found a sandwich! You ate it and gained 20 stamina points!", fg="green")
                root.update_idletasks()
                root.after(2000, lambda: animation_label.config(image=""))
                root.after(2000, lambda: message_label.config(text=""))
            elif event == "trap":
                stamina_points -= 20
                # Show warning animation
                animation_label.config(image=warning_photo)
                message_label.config(text="You encountered a trap! You tripped and lost 20 stamina points!", fg="red")
                root.update_idletasks()
                root.after(2000, lambda: animation_label.config(image=""))
                root.after(2000, lambda: message_label.config(text=""))

    return stamina_points



# Function to print the introduction one sentence at a time with prompt for user input
def print_intro(index=0):
    global animation_label, sandwich_photo, warning_photo, game_state, move_count  # Access the global variables
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
        enable_arrow_key()
        if move_count == 0:
            message_label.config(text="Please use the buttons or arrow keys to move.", fg="blue")
            root.update_idletasks()
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

    # Prompt the player to answer the questions
    tk.Label(quiz_window, text="Answer these art questions to continute:").pack()


    # List to store question labels to reference later
    question_labels = []

    # Function to check the quiz answers
    def check_answers():
        nonlocal question_labels  # Access the local variable in the outer scope

        global quiz_attempts, stamina_points, message_label, stamina_label, game_state

        # Get the selected answer for each question
        selected_answers = [var.get() for var in answer_vars]

        # List to store incorrect question indices
        incorrect_questions = []

        # Check if any question is left unanswered
        unanswered_questions = [i+1 for i, selected_answer in enumerate(selected_answers) if not selected_answer]
        if unanswered_questions:
            message_label.config(text="Please answer questions {} and try again.".format(", ".join(map(str, unanswered_questions))), fg="red")
            return

        # Check if all answers are correct
        for index, (selected_answer, question) in enumerate(zip(selected_answers, QUIZ_QUESTIONS)):
            if selected_answer != question["correct_answer"]:
                incorrect_questions.append(index)
        
        # Update the message label to show which question(s) were incorrect and deduct 20 stamina points
        if incorrect_questions:
            stamina_points -= 10
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label

            incorrect_question_text = "Question(s) {} are incorrect. You lost 10 stamina points.".format(
                ", ".join(str(i+1) for i in incorrect_questions))

            message_label.config(text=incorrect_question_text, fg = "red")
            root.update_idletasks()

            if stamina_points <= 0:
                handle_stamina_zero()
        else:
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_points += 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="You completed the quiz and got 20 stamina!", fg = "green")
            root.after(2000, lambda: message_label.config(text=""))

            # Disable the "Check Answers" button after the quiz is completed
            check_button.config(state="disabled")

            quiz_window.destroy()

            # Display the "Impressive!" message above the board one sentence at a time
            print_after_quiz_text()

    # Create answer variables for each question
    answer_vars = [tk.StringVar() for _ in QUIZ_QUESTIONS]

    # Create quiz questions and answer options
    for index, question in enumerate(QUIZ_QUESTIONS):
        question_frame = tk.Frame(quiz_window)
        question_frame.pack(pady=10)

        question_label = tk.Label(question_frame, text=question["question"])
        question_label.pack()
        question_labels.append(question_label)  # Store question label for later reference

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
        enable_arrow_key()

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
    quiz_window.title("Secret Room")

    # List to store question labels to reference later
    question_labels = []

    # Function to check the quiz answers
    def check_secret_answers():
        nonlocal question_labels  # Access the local variable in the outer scope

        global quiz_attempts, stamina_points, message_label, stamina_label, game_state

        # Get the selected answer for each question
        selected_answers = [var.get() for var in secret_answer_vars]

        # List to store incorrect question indices
        incorrect_questions = []

        # Check if any question is left unanswered
        unanswered_questions = [i+1 for i, selected_answer in enumerate(selected_answers) if not selected_answer]
        if unanswered_questions:
            message_label.config(text="Please answer questions {} and try again.".format(", ".join(map(str, unanswered_questions))), fg="red")
            return

        # Check if all answers are correct
        for index, (selected_answer, question) in enumerate(zip(selected_answers, SECRET_ROOM_QUIZ_QUESTIONS)):
            if selected_answer != question["correct_answer"]:
                incorrect_questions.append(index)

        # Update the message label to show which question(s) were incorrect and deduct 20 stamina points
        if incorrect_questions:
            stamina_points -= 10
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label

            incorrect_question_text = "Question(s) {} are incorrect. You lost 10 stamina points.".format(
                ", ".join(str(i + 1) for i in incorrect_questions))

            message_label.config(text=incorrect_question_text, fg = "red")
            root.update_idletasks()

            if stamina_points <= 0:
                handle_stamina_zero()
        else:
            # Player answered all questions correctly
            stamina_points = handle_event_with_animation(stamina_points, False)  # Update stamina (no animation after the quiz)
            stamina_points += 20
            stamina_label.config(text="Stamina: {}".format(stamina_points))  # Update the stamina label
            message_label.config(text="You completed the secret room quiz and got 20 stamina!", fg = "green")
            root.after(2000, lambda: message_label.config(text=""))

            # Disable the "Check Answers" button after the quiz is completed
            check_secret_button.config(state="disabled")

            # Destroy the quiz window after a delay
            quiz_window.destroy()

            # Display the "Unbelievable! You made it through all the challenges successfully!" message above the board one sentence at a time
            print_after_secret_room_quiz_text()

    # Create answer variables for each secret room quiz question
    secret_answer_vars = [tk.StringVar() for _ in SECRET_ROOM_QUIZ_QUESTIONS]

    # Create secret room quiz questions and answer options
    for index, question in enumerate(SECRET_ROOM_QUIZ_QUESTIONS):
        secret_question_frame = tk.Frame(quiz_window)
        secret_question_frame.pack(pady=10)

        question_label = tk.Label(secret_question_frame, text=question["question"])
        question_label.pack()
        question_labels.append(question_label)  # Store question label for later reference

        # Create answer options
        for option in question["options"]:
            tk.Radiobutton(secret_question_frame, text=option, variable=secret_answer_vars[index], value=option).pack(anchor="w")

    # Create a button to check answers
    check_secret_button = tk.Button(quiz_window, text="Check Answers", command=check_secret_answers)
    check_secret_button.pack(pady=10)

    # Update the game state to "secret_room" while the secret room quiz is displayed
    game_state = "secret_room"



def print_after_secret_room_quiz_text(index=0):
    if index < len(AFTER_SECRET_ROOM_QUIZ_TEXT):
        intro_label.config(text=AFTER_SECRET_ROOM_QUIZ_TEXT[index] + "\n\nPress Enter to continue")
        root.bind("<Return>", lambda event, i=index: print_after_secret_room_quiz_text(i + 1))
    else:
        intro_label.config(text="")
        root.unbind("<Return>")  # Unbind the Enter key after the text is displayed

        # Display the thank you message after the secret room quiz is over
        print_thank_you_message()



def print_thank_you_message():
    # Clear all elements from the GUI
    for widget in root.winfo_children():
        widget.destroy()
    # Create a blank label to display the thank you message
    thank_you_label = tk.Label(root, text="Thank you for playing the game!\n\nI hope you enjoyed the adventure!")
    thank_you_label.pack()


def handle_stamina_zero():
    # Clear all elements from the GUI
    for widget in root.winfo_children():
        widget.destroy()

    # Create a blank label to display the message
    stamina_zero_label = tk.Label(root, text="", wraplength=400)
    stamina_zero_label.pack()

    # List of lines to be displayed one at a time
    message_lines = [
        "Oh no! You've lost all your stamina. You fainted and were sent home by the school nurse.",
        "Your search for Irene has sadly ended, and now you will never know what happened to her...",
        "Thank you for playing the game!"
    ]

    message_lines_2 = [
        "Oh no! You failed to complete the final quiz and lost all of your stamina.",
        "Mr. Scrooge locked you up and his secret society took control over Onslow.",
        "Sadly, your journey to bring back Irene was not successful.",
        "GAME OVER."
    ]

    # Function to display the lines one at a time
    def display_line(index=0):
        if index < len(message_lines):
            stamina_zero_label.config(text=message_lines[index] + "\n\nPress Enter to continue")
            root.bind("<Return>", lambda event, i=index: display_line(i + 1))
        else:
            root.unbind("<Return>")  # Unbind the Enter key after the text is displayed
            print_thank_you_message()  # Display the thank you message after the stamina zero message is over
    def display_line_2(index=0):
        if index < len(message_lines_2):
            stamina_zero_label.config(text=message_lines_2[index] + "\n\nPress Enter to continue")
            root.bind("<Return>", lambda event, i=index: display_line_2(i + 1))
        else:
            root.unbind("<Return>")  # Unbind the Enter key after the text is displayed
            print_thank_you_message()  # Display the thank you message after the stamina zero message is over


    # Start displaying the lines
    if move_count == 11:
        display_line_2()
    else:
        display_line()

# Create the main window
root = tk.Tk()
root.title("Where in Onslow College is Irene Indiana")

# Function to handle arrow key movements
def on_arrow_key(event):
    if event.keysym == "Up":
        on_choice_button_click(OPTIONS["Move up 1 square"])
    elif event.keysym == "Down":
        on_choice_button_click(OPTIONS["Move down 1 square"])
    elif event.keysym == "Left":
        on_choice_button_click(OPTIONS["Move left 1 square"])
    elif event.keysym == "Right":
        on_choice_button_click(OPTIONS["Move right 1 square"])

# Bind the arrow keys to the on_arrow_key function
def enable_arrow_key():
    root.bind("<Up>", on_arrow_key)
    root.bind("<Down>", on_arrow_key)
    root.bind("<Left>", on_arrow_key)
    root.bind("<Right>", on_arrow_key)

# Add this function to display the "cannot move" message
def display_cannot_move_message():
    global message_label
    message_label.config(text="You cannot move right now. Please finish your current event and try again.", fg="red")
    root.update_idletasks()
    root.after(2000, lambda: message_label.config(text=""))

# Create and place the direction label
direction_label = tk.Label(root, text="Please pick a direction to move in")

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