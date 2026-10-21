try:
    number = int(input("Number"))
    result = 10 / number
except ValueError:
    print("Error: Value is wrong")
except ZeroDivisionError:
    print("Error: Division by zero.")
finally:
    print("This will always print.")
