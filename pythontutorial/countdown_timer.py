import time 

current_time = int(input("Enter the time in seconds : "))     # getting the time from consumer 

for t in range (current_time, -1, -1) :
    hours = int(t / 3600)                                     #calculating hours 
    minutes = int((t / 60) % 60)                              #calculating minutes
    seconds = t % 60                                          #calculating seconds 
    print(f"{hours :02}:{minutes :02}:{seconds :02}")
    time.sleep(1)                                             # waiting 1 second

print("Time is up! Wake UP!")

