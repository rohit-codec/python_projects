import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE
        )
        self.display.pack(fill="x", padx=10, pady=10, ipady=10)

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "%", "+"],
            ["√", "x²", "=", ""]
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both", padx=10, pady=5)

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if not text:
                    continue

                button = tk.Button(
                    frame,
                    text=text,
                    font=("Arial", 18),
                    command=lambda value=text: self.button_click(value)
                )
                button.grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=3,
                    pady=3
                )

        for i in range(6):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)

        root.bind("<Return>", lambda event: self.calculate())
        root.bind("<Escape>", lambda event: self.clear())

    def button_click(self, value):
        if value == "C":
            self.clear()
        elif value == "⌫":
            self.backspace()
        elif value == "=":
            self.calculate()
        elif value == "√":
            self.square_root()
        elif value == "x²":
            self.square()
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def calculate(self):
        try:
            expr = self.expression.replace("×", "*").replace("÷", "/").replace("−", "-")
            result = eval(expr, {"__builtins__": None}, {"math": math})

            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")
            self.clear()

    def square_root(self):
        try:
            value = float(self.expression)
            if value < 0:
                raise ValueError
            result = math.sqrt(value)
            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        except Exception:
            messagebox.showerror("Error", "Enter a valid non-negative number.")
            self.clear()

    def square(self):
        try:
            value = float(self.expression)
            result = value ** 2
            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        except Exception:
            messagebox.showerror("Error", "Enter a valid number.")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
