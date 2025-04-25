# Import required modules
import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("450x400")

# Add a title label
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
title_label.pack(pady=10)

# Step 4: Define the function to play the game
def play(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result =f"Both chose {player_choice} - It's A Tie!"
        color = "blue"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock")  or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result =f" You chose {player_choice}, computer chose {computer_choice} - You win ! 🎉"
        color = "green"
    else:
        result = f"You chose {player_choice}, Computer chose {computer_choice} - You lose 😢"
        color = "red"

    result_label.config(text=result, fg=color)

# Step 5: Add buttons for Rock, Paper, and Scissors
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button =tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Step 6: Create a label to show the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Step 7: Run the app
root.mainloop()