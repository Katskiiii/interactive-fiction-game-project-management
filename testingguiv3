import random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# ... (rest of the code)

# Load sandwich and warning images
sandwich_img = Image.open("sandwich.png")
sandwich_img = sandwich_img.resize((50, 50))  # Resize the image
sandwich_photo = ImageTk.PhotoImage(sandwich_img)

warning_img = Image.open("warning.png")
warning_img = warning_img.resize((50, 50))  # Resize the image
warning_photo = ImageTk.PhotoImage(warning_img)

# Function to handle finding items or encountering traps with animation
def handle_event_with_animation(stamina_points):
    if random.random() <= 0.1:
        event = random.choice(["item", "trap"])
        if event == "item":
            if stamina_points > 80:
                stamina_points = min(stamina_points + 20, 100)
            elif stamina_points <= 80:
                print("You found a sandwich! You gained 20 stamina points!")
                stamina_points += 20
                # Show sandwich animation
                animation_label.config(image=sandwich_photo)
                root.update_idletasks()
                root.after(1500, lambda: animation_label.config(image=""))
            elif stamina_points == 100:
                print("You found a sandwich but you weren't hungry and threw it away.")
        elif event == "trap":
            print("You encountered a trap! You lost 20 stamina points!")
            stamina_points -= 20
            if stamina_points <= 0:
                raise ValueError
            # Show warning animation
            animation_label.config(image=warning_photo)
            root.update_idletasks()
            root.after(1500, lambda: animation_label.config(image=""))
    return stamina_points

# ... (rest of the code)
