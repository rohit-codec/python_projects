import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        title = tk.Label(
            root, text="Tic Tac Toe",
            font=("Arial", 24, "bold"), pady=10
        )
        title.pack()

        self.status = tk.Label(
            root, text="Player X's Turn",
            font=("Arial", 14)
        )
        self.status.pack(pady=(0, 10))

        board_frame = tk.Frame(root)
        board_frame.pack(padx=15, pady=5)

        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 28, "bold"),
                width=4,
                height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=3, pady=3)
            self.buttons.append(button)

        tk.Button(
            root,
            text="New Game",
            font=("Arial", 12, "bold"),
            command=self.reset_game,
            padx=15,
            pady=5
        ).pack(pady=15)

    def make_move(self, index):
        if self.board[index] != "":
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
            return

        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (
                self.board[a] != "" and
                self.board[a] == self.board[b] == self.board[c]
            ):
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status.config(text="Player X's Turn")

        for button in self.buttons:
            button.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
