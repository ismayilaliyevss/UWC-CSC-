import random 
lowest = 1 
highest = 100
number = random.randint(lowest, highest)
  
print(number) #getting random number between 1 and 20 

number2 = random.random()   #giving random float number between 0 and 1 
print(number2)

options = ("rock", "paper", "scissors")

option = random.choice(options)  #getting random choice from options
print(option)

cards = ["1","2", "3", "4", "A", "B", "C", "D"]
random.shuffle(cards)   #gettind random order 
print(cards)

