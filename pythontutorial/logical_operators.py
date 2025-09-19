temp = int(input("Enter the temperature: "))
if temp > 35 or temp < 0 :
    print("Football match is cancelled")
else :
    is_it_raining = (input("Is it raining (0/1): "))
    is_it_raining = bool(int(is_it_raining))
    if is_it_raining :
        print("Football match is cancelled")

    else :     
        print("Go and PLAY football")

temperature = int(input("Enter the temperature: "))
is_it_sunny = bool(input("Is it sunny (0/1): "))

if temperature >= 30 and is_it_sunny == True :
    print("It is HOT outside")
    print("It is sunny")
elif temperature < 0 and is_it_sunny == True :
    print("It is COLD outside")
    print("It is sunny")
elif temperature >= 30 and is_it_sunny == False : 
    print("It is HOT outside")
    print("It is cloudy")
else :
    print("It is COLD outside")
    print("It is cloudy")