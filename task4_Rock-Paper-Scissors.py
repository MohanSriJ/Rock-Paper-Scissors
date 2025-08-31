import tkinter as tk
import random

# Choices with Emojis
choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

# Score Tracker
scores = {"user": 0, "computer": 0}

# Game Logic
def play(user_choice):
    computer_choice = random.choice(list(choices.keys()))

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "🎉 You Win!"
        scores["user"] += 1
    else:
        result = "💻 Computer Wins!"
        scores["computer"] += 1

    # Update UI
    user_label.config(text=f"You: {choices[user_choice]} ({user_choice})")
    comp_label.config(text=f"Computer: {choices[computer_choice]} ({computer_choice})")
    result_label.config(text=result)
    score_label.config(text=f"🏆 Score → You: {scores['user']} | Computer: {scores['computer']}")

# Reset Game
def reset_game():
    scores["user"] = 0
    scores["computer"] = 0
    user_label.config(text="You: ❔")
    comp_label.config(text="Computer: ❔")
    result_label.config(text="Result will appear here 🤔")
    score_label.config(text="🏆 Score → You: 0 | Computer: 0")

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors ✊✋✌️")
root.geometry("450x500")
root.config(bg="#1e1e2e")

# Title
title_label = tk.Label(root, text="🎮 Rock Paper Scissors 🎮", font=("Arial", 20, "bold"), fg="#f1fa8c", bg="#1e1e2e")
title_label.pack(pady=20)

# Labels
user_label = tk.Label(root, text="You: ❔", font=("Arial", 16), fg="#ffffff", bg="#1e1e2e")
user_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer: ❔", font=("Arial", 16), fg="#ffffff", bg="#1e1e2e")
comp_label.pack(pady=10)

result_label = tk.Label(root, text="Result will appear here 🤔", font=("Arial", 16, "bold"), fg="#8be9fd", bg="#1e1e2e")
result_label.pack(pady=15)

score_label = tk.Label(root, text="🏆 Score → You: 0 | Computer: 0", font=("Arial", 14), fg="#50fa7b", bg="#1e1e2e")
score_label.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="✊ Rock", font=("Arial", 14, "bold"), width=10, bg="#ffb86c",
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="✋ Paper", font=("Arial", 14, "bold"), width=10, bg="#ff79c6",
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✌️ Scissors", font=("Arial", 14, "bold"), width=10, bg="#bd93f9",
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 14, "bold"), width=15, bg="#6272a4", fg="white",
                      command=reset_game)
reset_btn.pack(pady=20)

# Footer
footer_label = tk.Label(root, text="Made with ❤️ in Python", font=("Arial", 12), fg="#ff5555", bg="#1e1e2e")
footer_label.pack(side="bottom", pady=10)

# Run App
root.mainloop()
