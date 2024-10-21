questions = ("How many planets are there in our solar system? ",
             "How many continents are there? ",
             "Who is currently leading the F1 World Driver's Championship? ",
             "What is the biggest ocean on Earth? ",
             "What team will Lewis Hamilton drive for in 2025? ")

options = (("A. 8", "B. 5", "C. 10", "D. 7"),
           ("A. 5", "B. 6", "C. 11", "D. 7"),
           ("A. Lando", "B. Lewis", "C. Ocon", "D. Max"),
           ("A. Pacific", "B. Atlantic", "C. Indian", "D. Arctic"),
           ("A. Mercedes", "B. Red bull", "C. Ferrari", "D. Williams"))

answers = (("A"), ("D"), ("D"), ("A"), ("C"))
guesses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Eter your answer to the question (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("        Results             ")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")