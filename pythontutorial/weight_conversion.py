weight = float(input("Enter your weight: "))
unit = input("L(bs) or K(gs) (L/K): ")

if unit == "L" :
    weight = weight / 2.05
    unit =  "LBS"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "K" :
    weight = weight * 2.05
    unit = "KGS"
    print(f"Your weight is {round(weight, 2)} {unit}")
else :
    print(f"Write a valid unit, {unit} is not valid")
    
    
