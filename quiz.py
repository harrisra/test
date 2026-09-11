"""A simple multiple-choice quiz game."""

import random

QUESTIONS = [
    {
        "question": "What does 'len([1, 2, 3])' return in Python?",
        "options": ["2", "3", "4", "Error"],
        "answer": "3",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def",
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris",
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["list", "dict", "set", "tuple"],
        "answer": "tuple",
    },
    {
        "question": "What is 7 * 6?",
        "options": ["36", "42", "48", "56"],
        "answer": "42",
    },
]


def ask_question(number, total, question):
    print(f"\nQuestion {number}/{total}: {question['question']}")
    options = question["options"][:]
    random.shuffle(options)
    for idx, option in enumerate(options, start=1):
        print(f"  {idx}. {option}")

    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return options[int(choice) - 1] == question["answer"]
        print("Please enter a number from 1 to 4.")


def run_quiz():
    print("=== Python Quiz ===")
    questions = QUESTIONS[:]
    random.shuffle(questions)

    score = 0
    for i, q in enumerate(questions, start=1):
        if ask_question(i, len(questions), q):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q['answer']}")

    print(f"\nYou scored {score}/{len(questions)}!")


if __name__ == "__main__":
    run_quiz()
