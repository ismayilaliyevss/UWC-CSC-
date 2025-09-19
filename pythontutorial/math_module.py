import math

x = 9
y = 2.5
z=3.7

print(math.pi)
print(math.e)
result1 = math.sqrt(x)
print(result1)
result2 = math.ceil(y)
print(result2)
result3 = math.floor(z)
print(result3)

# exercise 1 circumference of a circle 

radius = input("Enter the radius of the circle:")

circumference = float(2) * math.pi * float(radius)

print(f"The circumference of the circle is: {round (circumference, 2)}")

# exercise 2 area of a circle

radius = input("Enter the radius of the circle:")

area = (math.pi * float(radius) **2)

print(f"The area of the cirrcle is: {round(area, 2)} cm^2")

# exercise 3 hypotenuse of a right triangle

a = input("Enter the length of first side :")
b = input("Enter the length of the second side :")
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of the hypotenuse is : {round(c, 2)} cm")
