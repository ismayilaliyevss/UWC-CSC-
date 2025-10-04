import random 

options = ("rock", "paper", "scissors")
running = True
while running :
    player = " "
    computer = random.choice(options)

    
    while player not in options :
        player = input("Enter a choice from rock, paper and scissors: ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer :
        print("It is a tie! Continue")
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock") : 
        print("Congrats! You WON!")
    else :
        print("You LOSE! HAHAHA")

    if input("Play again? (y/n): ").lower() != "y" :
        running = False

print("Thanks for playing!!!")