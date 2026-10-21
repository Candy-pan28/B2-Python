# 17 project: compound interest calculator
# formula: A = P * (1 + r/100) ** t
principal = float(input("The principle is: "))
rate = float(input("The annual rate is(eg.4): "))
years = int(input("The number of years: "))
while principal <= 0 or rate < 0 or years < 0: #prevent input problem
    print("the principle must larger 0, rate and years can not be negative")
    principal = float(input("The principle is: "))
    rate = float(input("The annual rate is: "))
    years = int(input("The number of years: "))
total = principal * (1 + rate / 100) ** years
print(f"The number of money{total}")