
questions = [
    {
        "question": "1. What is the output of 5 ** 2?",
        "options": ["A. 10", "B. 25", "C. 15", "D. 20"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword defines a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "3. Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "4. What does len('Python') return?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "5. Which loop iterates over a sequence?",
        "options": ["A. for", "B. if", "C. def", "D. class"],
        "answer": "A"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", q["answer"])

print("\n===== QUIZ RESULT =====")
print("Your score:", score, "/", len(questions))
print("Percentage:", round(score / len(questions) * 100, 2), "%")
