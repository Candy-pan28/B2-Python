#22 Shopping cart
things = []
total = 0
prices = []

while True: #if the conditions are true, keep circulation
    thing = str(input("Enter a commodity to buy (q to quit): "))
    if thing == "q":
        break

    price = float(input(f"Enter the price of a {thing}(unit:$): "))
    if price<0:
        print("The price should not be negative")
        continue

    things.append(thing) # add things and prices
    prices.append(price)

print("----- YOUR CART -----")

for thing in things:
    print(thing, end=" ") #add a space after print things instead of change row

for price in prices:
    total = total + price

print(f"Your total is: {total}$")