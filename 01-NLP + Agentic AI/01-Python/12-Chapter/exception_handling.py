try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"The result of {a} divided by {b} is {result}")
except ValueError as v:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError as x:
    print("Error: Division by zero is not allowed.")