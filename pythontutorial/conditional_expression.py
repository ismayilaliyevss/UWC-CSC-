num = input("Enter the number: ")
a = input("Enter the number a: ")
b = input("Enter the number b: ")
age = input("Enter your age: ")
temp = input("Enter the temp: ")

num = int(num)
print( "Positive" if num>0 else "Negative")

result = "Even" if num%2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
min_num = a if a<b else b
print(f"Max number is {max_num}")
print(f"Min number is {min_num}")

age = int(age)
profile = "Adult" if age >=18 else "Drink your milk!"
print(profile)

weather = "Hot" if int(temp) > 30 else "Cold"
print(weather)
