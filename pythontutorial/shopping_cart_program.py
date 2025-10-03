meals = []
prices = []
total = 0

while True :
    food = input("Enter food to buy (a to quit): ")
    if food.lower() == 'a' :                                # for using both a and A 
        break
    else :
        meals.append(food)                                  #adding new value
        price = float(input(f"Enter the price of {food} : $"))
        prices.append(price)                                    #adding new value 

print("---- YOUR CARD BALANCE ----")

for food in meals :
    print(food, end=" ")

print()

for price in prices :
    total+= price                               
                        
print(f"Total fee is: ${total :.2f}")                   #rounding total price to 2 decimal points
    