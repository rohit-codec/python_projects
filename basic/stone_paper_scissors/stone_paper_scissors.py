import tkinter as tk
from random import choice

CHOICES = ["Stone", "Paper", "Scissors"]


def get_result(player, computer):
    if player == computer:
        return "It's a Draw!"
    if (
        (player == "Stone" and computer == "Scissors")
        or (player == "Paper" and computer == "Stone")
        or (player == "Scissors" and computer == "Paper")
    ):
        return "You Win!"
    return "Computer Wins!"


class StonePaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Stone Paper Scissors")
        self.root.geometry("500x520")
        self.root.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

        tk.Label(
            root,
            text="STONE • PAPER • SCISSORS",
            font=("Arial", 20, "bold"),
        ).pack(pady=(25, 10))

        tk.Label(
            root,
            text="Choose your move",
            font=("Arial", 13),
        ).pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        for item in CHOICES:
            tk.Button(
                button_frame,
                text=item,
                width=12,
                height=2,
                font=("Arial", 11, "bold"),
                command=lambda move=item: self.play(move),
            ).pack(pady=6)

        self.player_label = tk.Label(
            root, text="You: -", font=("Arial", 14)
        )
        self.player_label.pack(pady=5)

        self.computer_label = tk.Label(
            root, text="Computer: -", font=("Arial", 14)
        )
        self.computer_label.pack(pady=5)

        self.result_label = tk.Label(
            root, text="Make your move!", font=("Arial", 16, "bold")
        )
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(
            root,
            text="Score  |  You: 0   Computer: 0   Draws: 0",
            font=("Arial", 12),
        )
        self.score_label.pack(pady=10)

        tk.Button(
            root,
            text="Reset Game",
            width=15,
            height=2,
            command=self.reset,
        ).pack(pady=15)

    def play(self, player_choice):
        computer_choice = choice(CHOICES)
        result = get_result(player_choice, computer_choice)

        self.player_label.config(text=f"You: {player_choice}")
        self.computer_label.config(text=f"Computer: {computer_choice}")
        self.result_label.config(text=result)

        if result == "You Win!":
            self.player_score += 1
        elif result == "Computer Wins!":
            self.computer_score += 1
        else:
            self.draws += 1

        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=(
                f"Score  |  You: {self.player_score}   "
                f"Computer: {self.computer_score}   "
                f"Draws: {self.draws}"
            )
        )

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

        self.player_label.config(text="You: -")
        self.computer_label.config(text="Computer: -")
        self.result_label.config(text="Make your move!")
        self.update_score()


if __name__ == "__main__":
    root = tk.Tk()
    app = StonePaperScissors(root)
    root.mainloop()
