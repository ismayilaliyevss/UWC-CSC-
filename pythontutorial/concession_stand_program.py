menu = {"doner" : 3.5,
        "kebap" : 7.6,
        "pizza" : 8.5,
        "burger" : 5.4,
        "fanta" : 2.2,
        "ayran" : 3.0}

cart = []
total = 0

print("--------- MENU ---------")

for key, value in menu.items() :
    print(f"{key :10} : ${value :.2f}")                 #printing the menu in order

print("------------------------")

while True :
    food = input("Enter your food (a to quit) :").lower()
    if food == 'a' :
        break
    elif menu.get(food) is not None :
        cart.append(food)
        total+=menu.get(food)

print("------- YOUR MEAL -------")
for meal in cart :
    print(meal, end= " ")
print()
print(f"Total is: ${total:.2f}")
