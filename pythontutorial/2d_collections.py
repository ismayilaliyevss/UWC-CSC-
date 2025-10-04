fruits =     ["apple", "pineapple", "cherry", "banana"]
vegetables = ["cucumber", "tomato", "carrots"]
meats =      ["fish", "chicken", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)

cars = [["bmw", "audi", "merc"],
        ["byd", "changhan"],
        ["tesla", "ford", "dodge"]]

for collection in cars :
    for car in collection :
        print(car, end=" ")
    print()

#keypad exercise 

num_pad = ((1 , 2 , 3),
           (4 , 5 , 6),
           (7 , 8 , 9),
           ('*', 0 , '#'))
   
for row in num_pad :
    for number in row :
        print(number, end=" ")
    print()                         #going to a new line after every row 
