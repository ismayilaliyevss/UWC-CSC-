pr1 = 500000.4567
pr2 = -7456.89
pr3 = 23.32

print(f"Price one is {pr1 : .2f}") # .(number)f - round to that many decimal places
print(f"Price two is {pr2 : 10}") # (number) - allocote that many spaces
print(f"Price three is {pr3 : 010}") # 0(number) - fill with leading zeros to that many spaces
print(f"Price one is {pr1 : <10}") # < - left align 
print(f"Price two is {pr2 : >10}") # > - right align
print(f"Price three is {pr1 : ^10}") # ^ - center align
print(f"Price one is {pr1 : +}") # + - use + sign for positive numbers
print(f"Price two is {pr2 : =}") # =  - place the sign to the left most position
print(f"Price three is {pr3 : }") #   - use a space for positive numbers
print(f"Price one is {pr1 : ,}") # , - use comma as a thousand separator
number = 34567.7896
print(f"number is equal to {number :+<10,.3f}")