# Using walrus operator

if (n := len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")