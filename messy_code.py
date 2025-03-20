def calculate_total():
    x = 1
    y = 2
    for i in range(100):  # Deeply nested loops
        for j in range(100):
            print(x + y)  # No error handling
    z = x + y  # Unused variable
