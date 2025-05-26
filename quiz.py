import time
questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars"],
        "answer": "B",
        "explanation": "Mars is called the Red Planet due to its reddish appearance."
    },
    {
        "question": "Who was the first President of the USA?",
        "options": ["A. Abraham Lincoln", "B. George Washington"],
        "answer": "B",
        "explanation": "George Washington was the first President of the United States."
    },
    {
        "question": "How many players are there in a football (soccer) team?",
        "options": ["A. 11", "B. 9"],
        "answer": "A",
        "explanation": "Each football team has 11 players on the field."
    }]
score = 0
total_questions = len(questions)

print("🧠 Welcome to the Quiz Game!")
print("You have 10 seconds to answer each question.\n")
question_number = 1
for q in questions:
    print(f"Q{question_number}: {q['question']}")
    for opt in q['options']:
        print(opt)
    start = time.time()
    answer = input("Your answer (A/B): ").strip().upper()
    end = time.time()
    if end - start > 10:
        print("⏰ Time's up! You took too long.\n")
    elif answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.")
        print(f"💡 Explanation: {q['explanation']}\n")
    question_number += 1  
percentage = (score / total_questions) * 100
print("🎯 Quiz Complete!")
print(f"Your score: {score} out of {total_questions}")
print(f"Percentage: {percentage:.2f}%")
if percentage == 100:
    print("🏆 Excellent! Perfect score!")
elif percentage >= 60:
    print(" Good job! Keep practicing.")
else:
    print("🔁 Try again! You can do better.")
