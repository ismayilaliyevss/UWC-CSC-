temp = float(input("Enter the temperature: "))
unit = input("C or F (C/F): ")

if unit == "C" :
    temp = (temp * 9/5)+32
    unit = "F"
    print(f"Temperature is {round(temp, 2)} {unit}")
elif unit == "F" :
    temp = (temp - 32) * 5/9
    unit = "C"
    print(f"Temperature is {round(temp, 2)} {unit}")
else :
    print(f"Write a valid unit, {unit} is not valid")
    
    
