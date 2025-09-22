name = input("Enter your name: ")
phone_number = input("Enter your number : ")


result = len(name)
print(result)

result = name.find("I")
print(result)


result = name.rfind("i")
print(result)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

result1 = name.isdigit()
print(result1)

result1 = name.isalpha()  # -> only letters
print(result1)

result = phone_number.count("0")
print(result)

phone_number = phone_number.replace("0" , "5")
print(phone_number)

print(help(str)) # -> ALL functions about STRINGS

# exercise 
username = input("Enter your username :")

size_of_username = len(username)
result1 = username.find(" ")
result2 = username.isdigit()

if size_of_username > 12 :
    print("Username is not valid")
elif result1 >0 :
    print("Username is not valid")
elif result2 == True :
    print("Username is not valid")
else :
    print("Your username succesfully created!")
 