# python quiz
question = ("How to capitalize alphabets in python?",
            "How to convert from float to string type in python?",
            "How many types of collection are there?",
            "How to quick copy-paste?")
options = (("a. using upper() method","b. using lower() method","c. using title() method","d. using capitalize() method"),
           ("a. using type()","b. using str()","c. using int()","d. using float()"),
           ("a. 1","b. 2","c. 3","d. 4"),
           ("a. ctrl+C","b. ctrl+V","c. Both a and b","d. N.O.T"))
answers = ("d","b","d","c")
guesses = []
score = 0
question_num = 0
for questions in question:
    print("------------------------------")
    print(questions)
    print()
    for option in options[question_num]:
        print(option, end=" ")
        
    guess = input("Enter (a,b,c,d):").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")     
    else:
        print("Wrong!")
        print(f"The correct answer is: {answers[question_num]}")

    question_num += 1
    print(f"Your score is: {score}/4")
