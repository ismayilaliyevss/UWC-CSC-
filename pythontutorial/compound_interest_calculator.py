present_value = 0
rate = 0 
time = 0

while True :
    present_value = float(input("Enter the present value :"))
    if present_value < 0 :
        print("Present value cannot be less than zero")
    else :
        break

while True :
    rate = float(input("Enter the rate :"))
    if rate < 0 :
        print("Rate cannot be less than zero")
    else :
        break

while True :
    time = int(input("Enter the time :"))
    if time < 0 :
        print("Time cannot be less than zero")
    else :
        break

future_value = present_value * pow((1 + rate / 100), time)

print(f"The Balance after {time} year/s : ${future_value : .2f}" )
