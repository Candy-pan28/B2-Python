#24 make a quiz, I use the same question in the video
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"))

answers = ("C", "D", "A")
guesses = []
score = 0
qn = 0

for question in questions: #print all the qs one by one
    print(question)
    for option in options[qn]:
        print(option)

    guess = str(input("Enter (A, B, C, D): ")).upper() #same format
    guesses.append(guess)
    if guess == answers[qn]:
        score = score + 1
        print("You are Correct!")
    else:
        print("Pity, you are incorrect!")
        print(f"{answers[qn]} is the correct answer")
    qn = qn + 1

print("       RESULTS        ")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")