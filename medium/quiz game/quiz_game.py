import json
import random
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

QUESTION_FILE = BASE_DIR / "questions.json"
SCORE_FILE = BASE_DIR / "scores.json"


def load_questions():
    with open(QUESTION_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def load_scores():
    if not SCORE_FILE.exists():
        return []
    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_score(name, score, total, category, difficulty):
    scores = load_scores()
    scores.append({
        "name": name,
        "score": score,
        "total": total,
        "percentage": round(score / total * 100, 1),
        "category": category,
        "difficulty": difficulty,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    scores.sort(key=lambda item: item["percentage"], reverse=True)
    scores = scores[:10]

    with open(SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)


def choose_option(title, options):
    print(f"\n{title}")
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Enter choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")


def choose_category(questions):
    categories = ["All"]
    categories += sorted({question["category"] for question in questions})
    return choose_option("Select Category", categories)


def choose_difficulty():
    return choose_option(
        "Select Difficulty",
        ["Easy", "Medium", "Hard", "Mixed"]
    )


def ask_question(question, number, total):
    print("\n" + "-" * 65)
    print(f"Question {number}/{total} | {question['category']} | "
          f"{question['difficulty']}")
    print(f"Points: {question['points']}")
    print(question["question"])

    options = question["options"]
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")

    while True:
        try:
            answer = int(input("Your answer: "))
            if 1 <= answer <= len(options):
                return answer - 1
        except ValueError:
            pass
        print("Enter a valid option number.")


def show_leaderboard():
    scores = load_scores()

    print("\n" + "=" * 65)
    print("LEADERBOARD - TOP 10")
    print("=" * 65)

    if not scores:
        print("No scores available yet.")
        return

    print(f"{'Rank':<6}{'Name':<18}{'Score':<10}{'%':<8}"
          f"{'Category':<15}{'Difficulty'}")

    for rank, item in enumerate(scores, 1):
        score_text = f"{item['score']}/{item['total']}"
        print(f"{rank:<6}{item['name'][:17]:<18}{score_text:<10}"
              f"{item['percentage']:<8}{item['category'][:14]:<15}"
              f"{item['difficulty']}")


def show_result(name, score, max_score, correct, total, category, difficulty):
    percentage = (score / max_score * 100) if max_score else 0

    print("\n" + "=" * 65)
    print("QUIZ RESULT")
    print("=" * 65)
    print(f"Player       : {name}")
    print(f"Category     : {category}")
    print(f"Difficulty   : {difficulty}")
    print(f"Correct      : {correct}/{total}")
    print(f"Score        : {score}/{max_score}")
    print(f"Percentage   : {percentage:.1f}%")

    if percentage >= 90:
        message = "Outstanding performance!"
    elif percentage >= 70:
        message = "Great job! Keep practicing."
    elif percentage >= 50:
        message = "Good attempt. Revise the weak topics."
    else:
        message = "Keep learning and try again."

    print(f"Feedback     : {message}")
    print("=" * 65)


def play_quiz(all_questions):
    name = input("\nEnter your name: ").strip() or "Player"

    category = choose_category(all_questions)
    difficulty = choose_difficulty()

    filtered = [
        q for q in all_questions
        if (category == "All" or q["category"] == category)
        and (difficulty == "Mixed" or q["difficulty"] == difficulty)
    ]

    if not filtered:
        print("No questions found for this combination.")
        return

    try:
        count = int(input(
            f"How many questions? (1-{min(10, len(filtered))}): "
        ))
        count = max(1, min(count, min(10, len(filtered))))
    except ValueError:
        count = min(10, len(filtered))
        print(f"Invalid input. Using {count} questions.")

    quiz = random.sample(filtered, count)
    score = 0
    correct = 0
    max_score = sum(q["points"] for q in quiz)

    start_time = time.time()

    for number, question in enumerate(quiz, 1):
        answer = ask_question(question, number, count)

        if answer == question["answer"]:
            print("Correct!")
            score += question["points"]
            correct += 1
        else:
            correct_answer = question["options"][question["answer"]]
            print(f"Wrong! Correct answer: {correct_answer}")

        # Show explanation after every question.
        print(f"Explanation: {question['explanation']}")

    elapsed = time.time() - start_time

    show_result(
        name, score, max_score, correct, count, category, difficulty
    )
    print(f"Time taken  : {elapsed:.1f} seconds")

    save_score(name, score, max_score, category, difficulty)
    print("Your score has been saved.")


def main():
    try:
        questions = load_questions()
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: questions.json is missing or invalid.")
        return

    while True:
        print("\n" + "=" * 65)
        print("                 PYTHON QUIZ MASTER")
        print("=" * 65)
        print("1. Start Quiz")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_quiz(questions)
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
