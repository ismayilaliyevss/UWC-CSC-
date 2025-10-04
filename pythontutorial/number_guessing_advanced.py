import random

lowest = int(input("Enter the lowest number: "))
highest = int(input("Enter the highest number: "))
answer = random.randint(lowest, highest)

guesses = 0
is_running = True

print("----------- Welcome to Python NUMBER GUEESSING GAME! -----------")
print("----------------------------------------------------------------")
print()
print(f"Select a number between {lowest} and {highest}")
while is_running :
    guess = (input("Enter your guess: "))
    if guess.isdigit() :
        guess = int(guess)
        guesses+=1

        if guess < lowest or guess > highest :
            print("The guess is out of range ")
            print(f"Please, select a number between {lowest} and {highest}")

        elif guess < answer :
            print(f"Your guess {guess} is too low")
            lowest = guess
            print(f"Select a number between {lowest} and {highest}")
        elif guess > answer :
            print(f"Your guess {guess} is too high")
            highest = guess
            print(f"Select a number between {lowest} and {highest}")
        else :
            print("----------------- CONGRATULATIONS! -----------------")
            print(f"Your guess {guess} is correct, it took {guesses} guesses")
            is_running = False
            
    else :
        print("The guess is not valid!")
        print(f"Please, select a number between {lowest} and {highest}")
    
