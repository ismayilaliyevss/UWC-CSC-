questions = ("Who is the current president of Azerbaijan? ",
              "Which one is the meal of Turkiye? ", 
              "What is the biggest country in the world? ", 
              "Which subject is the beginning of all subjects? ")

options = (("A) Haydar Aliyev", "B) Ilham Aliyev", "C) Ebulfaz Elcibay", "D) Recep Tayyip"),
           ("A) sarma", "B) bozbas", "C) pasta", "D) hamburger"),
           ("A) Canada", "B) USA", "C) Russia", "D) China"),
           ("A) Math", "B) Physics", "C) Biology", "D) Philosophy"))

answers = ("B", "A", "C", "D")
guesses= []
question_num = 0                                #for numbering 2d list
score = 0

for question in questions :
    print("-------------------------------")
    print(question)

    for option in options[question_num] :
        print(option)

    guess = input("Enter your answer (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num] :
        score+=1
        print("Correct!")
    else :
        print("Incorrect!")
        print(f"answer is {answers[question_num]}")
    question_num+=1

print("-------------------------------")
print("           RESULTS             ")
print("-------------------------------")

score = score / len(questions)
print(int(score*100))