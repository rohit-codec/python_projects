import tkinter as tk
import random

# -----------------------------
# Game Variables
# -----------------------------
number = random.randint(1, 100)
tries = 0


# -----------------------------
# Functions
# -----------------------------
def check_guess():
    global tries

    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number!")
        return

    if guess < 1 or guess > 100:
        result_label.config(text="⚠️ Enter a number between 1 and 100!")
        return

    tries += 1
    attempts_label.config(text=f"Attempts: {tries}")

    if guess < number:
        result_label.config(text="📈 The number is HIGHER!")
    elif guess > number:
        result_label.config(text="📉 The number is LOWER!")
    else:
        result_label.config(
            text=f"🎉 Correct! You guessed it in {tries} tries!"
        )
        guess_button.config(state="disabled")


def play_again():
    global number, tries

    number = random.randint(1, 100)
    tries = 0

    entry.delete(0, tk.END)
    result_label.config(text="🤔 Guess the number!")
    attempts_label.config(text="Attempts: 0")
    guess_button.config(state="normal")


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x400")
root.resizable(False, False)


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=25)


# -----------------------------
# Instructions
# -----------------------------
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 13)
)
instruction_label.pack(pady=5)


# -----------------------------
# Input
# -----------------------------
entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center",
    width=12
)
entry.pack(pady=20)

entry.focus()


# -----------------------------
# Guess Button
# -----------------------------
guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 13, "bold"),
    width=12,
    command=check_guess
)
guess_button.pack(pady=5)


# -----------------------------
# Result
# -----------------------------
result_label = tk.Label(
    root,
    text="🤔 Guess the number!",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)


# -----------------------------
# Attempts
# -----------------------------
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12)
)
attempts_label.pack()


# -----------------------------
# Play Again Button
# -----------------------------
play_again_button = tk.Button(
    root,
    text="PLAY AGAIN",
    font=("Arial", 12),
    command=play_again
)
play_again_button.pack(pady=20)


# -----------------------------
# Run Application
# -----------------------------
root.mainloop()
