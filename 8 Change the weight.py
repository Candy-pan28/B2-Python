#8 change the weight
weight = float(input("The weight is: "))
unit = input("The original unit is kg/lb: ").strip().lower() #change the input to same format
if weight < 0:
    print("The weight can't be negative")
elif unit == "kg":
    print(f"{weight / 0.45359237} lb") #change kg to lb and use f string to print
elif unit == "lb":
    print(f"{weight * 0.45359237} kg") #change lb to kg and use f string to print
else:
    print("The unit is unavailable")