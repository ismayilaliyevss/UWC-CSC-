#exercise number guessing game 
import random
low = 0 
high = 100 
guesses = 0
number = random.randint(low, high)
while True :
    guess = int(input(f"Enter a number between {low} and {high}: "))
    if guess < number :
        print(f"Your guess {guess  }is too low")
        low = guess
        guesses+=1
    elif guess > number :
        print(f"Your guess {guess } is too high")
        high = guess
        guesses+=1
    else :
        print(f"Your guess {guess} is correct, it took {guesses} guesses")
        break