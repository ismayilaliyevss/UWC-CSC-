# strings 
first_name = "Ismayil"
food = "burger"
mail = "ismayilaliyevs@yahoo.com"

print(first_name)

print(f"Hi {first_name}")
print(f"I like to eat {food}")
print(f"My email is: {mail}")

# integers
age = 16
quantity = 5
number_of_students = 12

print(f"I am {age} years old")
print(f"I am buying {quantity} {food}s")
print(f"My class has {number_of_students} people")

# float 
price = 5.99
gpa = 3.9
distance = 15.5 

print(f"The price is {price} manat")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance} kilometers")

#boolean 
is_Ismayil_graduated = False
is_Ismayil_a_good_student = True
for_sale = True
is_online = False

print(f"Are you graduated from high school? : {is_Ismayil_graduated}")

if is_Ismayil_a_good_student :
    print("You are a perfect student")
else :
    print("You need to listen to teachers!")
if for_sale :
    print("You can buy this item")
else :
    print("This item is NOT available")
if is_online :
    print("MY friend is online")
else :
    print("He is offline")

# final exam
user_name = "Bro Code"
year = 2025
pi = 3.14
is_admin = True

if is_admin : 
    print(f"Welcome {user_name} to pi ({pi}) world in year {year}")
else :
    print("Get out of this code!")