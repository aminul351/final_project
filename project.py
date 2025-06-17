def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().lower()
        if answer == q["answer"].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['answer']}\n")
    print(f"🎉 You got {score}/{len(questions)} questions right!")

# Define your questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Paris", "c) Madrid", "d) Rome"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
        "answer": "b"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) J.K. Rowling", "c) William Shakespeare", "d) Mark Twain"],
        "answer": "c"
    }
]

# Run the quiz
run_quiz(quiz_questions)
