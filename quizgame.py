questions = [
    {
        "prompt": "what is the capital of Nevada?",
        "options": ["A. Paris", "B. North Dakota", "C. Carson City", "D. Africa"],
        "answer": "C"
    },
    {
        "prompt": "what is 51 + 22?",
        "options": ["A. 70", "B. 90", "C. 1000", "D. 73"],
        "answer": "D"

    },
    {
        "prompt": "how many days are in one year?",
        "options": ["A. 271", "B. 365", "C. 12", "D. 52"],
        "answer": "B"
    },
    {
        "prompt": "What is July 4th considered in the United States?",
        "options": ["A. Passover", "B. Christmas", "C. Independence Day", "D. St. Patricks Day"],
        "answer": "C"
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct, way to go!\n")
            score += 1
        else:
            print("You absolutely suck, these questions are easy! The correct answer was", question["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")
    print(f"Your score is {score}")


run_quiz(questions)