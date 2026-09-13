# Stone Paper Scissors — Python GUI Game

A simple **Stone Paper Scissors** game built in Python using the built-in `tkinter` GUI library.

## Features

- Graphical user interface
- Player vs Computer gameplay
- Computer makes a random choice
- Displays both choices
- Shows Win / Lose / Draw result
- Keeps score
- Reset Game button
- No external Python packages required

## Requirements

- Python 3.x
- Tkinter

Tkinter is normally included with standard Python installations on Windows and macOS.

## Project Structure

```text
stone_paper_scissors/
├── stone_paper_scissors.py
└── README.md
```

## How to Run

1. Install Python 3 if it is not already installed.
2. Open a terminal or command prompt.
3. Navigate to the project folder.

```bash
cd stone_paper_scissors
```

4. Run the program:

```bash
python stone_paper_scissors.py
```

## Rules

The game follows the standard rules:

- **Stone beats Scissors**
- **Scissors beats Paper**
- **Paper beats Stone**
- Same choice = **Draw**

## How It Works

The program stores the three possible choices:

```python
CHOICES = ["Stone", "Paper", "Scissors"]
```

When the player clicks a button, the computer randomly selects one choice:

```python
computer_choice = choice(CHOICES)
```

The `get_result()` function compares the player's choice with the computer's choice and returns the result.

The GUI is created using `tkinter`, while the scores are stored as:

```python
self.player_score
self.computer_score
self.draws
```

## Technologies Used

- Python
- Tkinter
- Random module

## Future Improvements

Possible improvements include:

- Add images/icons for Stone, Paper and Scissors
- Add sound effects
- Add difficulty levels
- Add a best-of-3 or best-of-5 mode
- Add animations
- Add a game history
- Improve the visual design with custom themes
