name = input("Enter your name :")

while name == "" :
    print("You did not enter anything")
    name = input("Enter your name :")
print(f"Hi Mr/Mrs. {name}")  


age = int(input("Enter your age: "))

while age < 0 : 
    print("Age cannot be negative")
    age = int(input("Enter your age: "))
print(f"Hi, you are {age} years old ")


food = input("Enter your favourite food (a to escape) : ")

while not food == "a" :
    print(f"Okey, you like {food}")
    food = input("Enter another favourite one (a to escape) : ")
print("bye bye")

num = int(input("Enter a number between 1 and 10 :"))

while num < 1 or num > 10 :
    print("Your number is not valid")
    num = int(input("Enter a number between 1 and 10 :"))
print(f"Your number is {num}")