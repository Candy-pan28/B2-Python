#20 Countdown time in Python
import time #import python time module

total = int(input("The countdown time is(plz enter seconds): "))
for x in range(total, 0, -1): #let remaining every time decrease one
    hour = int(x / 3600)
    minute = int(x / 60) % 60
    second = x % 60
    print(f"{hour:02}:{minute:02}:{second:02}") #print all the numbers in 2 number
    time.sleep(1) #stop running the code for 1 second every row

print("Time is up!")