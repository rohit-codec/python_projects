# Python Quiz Master

A medium-level **Python Quiz Game** project built using core Python concepts, JSON data storage, randomization, file handling, and a leaderboard system.

## Features

- Menu-driven CLI
- Player name
- Multiple quiz categories
- Difficulty selection: Easy, Medium, Hard, Mixed
- Random questions
- Select number of questions
- Different points for different difficulty levels
- Instant answer checking
- Explanation after every question
- Score and percentage calculation
- Quiz time tracking
- Persistent top-10 leaderboard using JSON
- Input validation
- Questions stored separately in `questions.json`

## Project Structure

```text
python-quiz-game/
│
├── quiz_game.py
├── questions.json
├── scores.json          # Created automatically after playing
└── README.md
```

## Requirements

- Python 3.8+
- No external packages required.

## Run

Open the project folder in VS Code and run:

```bash
python quiz_game.py
```

## How It Works

### 1. Select Start Quiz

Enter your player name and select:

- Category
- Difficulty
- Number of questions

### 2. Answer Questions

Each question displays four options. Enter the option number.

The game immediately displays:

- Correct/wrong status
- Correct answer when wrong
- Explanation

### 3. Result

At the end, the program calculates:

- Number of correct answers
- Total score
- Maximum possible score
- Percentage
- Time taken

### 4. Leaderboard

The top 10 scores are stored in `scores.json`.

Scores are sorted according to percentage.

## Scoring System

| Difficulty | Points |
|---|---:|
| Easy | 1 |
| Medium | 2 |
| Hard | 3 |

This makes the game more interesting because difficult questions contribute more to the score.

## Python Concepts Used

This project demonstrates:

- Variables and data types
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- List comprehensions
- Sets
- File handling
- JSON
- Exception handling
- `random` module
- `time` module
- `pathlib`
- Sorting
- Input validation
- Modular program design

## Example Menu

```text
=================================================================
                 PYTHON QUIZ MASTER
=================================================================
1. Start Quiz
2. View Leaderboard
3. Exit
Choose an option:
```

## Example Result

```text
===============================================================
QUIZ RESULT
===============================================================
Player       : Rohit
Category     : All
Difficulty   : Mixed
Correct      : 7/10
Score        : 15/21
Percentage   : 71.4%
Feedback     : Great job! Keep practicing.
===============================================================
Time taken  : 42.5 seconds
Your score has been saved.
```

## Future Improvements

Possible upgrades for an advanced version:

- Tkinter GUI
- Countdown timer per question
- 50-50 lifeline
- Skip question
- Negative marking
- User login/signup
- SQLite database instead of JSON
- Admin panel to add/edit/delete questions
- Question import from CSV
- Charts for performance analysis
- Online multiplayer mode
- API-based question loading

## Author

Rohit

## License

Free to use for learning and educational purposes.
