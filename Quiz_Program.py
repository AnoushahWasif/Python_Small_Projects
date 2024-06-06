quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "options": "Paris",
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "options":  "Berlin",
    },
    "question3": {
        "question": "What is the capital of England?",
        "options":  "London",
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "options":  "Madrid",
    },
    "question5": {
        "question": "What is the capital of Italy?",
        "options":  "Rome",
    },
    "question6": {
        "question": "What is the capital of Portugal?",
        "options":  "Lisbon",
    },
    "question7": {
        "question": "What is the capital of Netherlands?",
        "options":  "Amsterdam",
    },
    "question8": {
        "question": "What is the capital of Belgium?",
        "options":  "Brussels",
    },
    "question9": {
        "question": "What is the capital of Greece?",
        "options":  "Athens",
    },
    "question10": {
        "question": "What is the capital of Turkey?",
        "options":  "Ankara",
    }
}

score = 0

for question in quiz:
    user_answer = input(quiz[question]["question"] + "\n")
    if user_answer.lower() == quiz[question]["options"].lower():
        score += 1
    else:
        print("Incorrect! The correct answer is " + quiz[question]["options"])
print("You scored " + str(score) + " out of 10")