import math

# Ask the user for a number
try:
    number = float(input("Enter a positive number: "))

    if number <= 0:
        print("Please enter a number greater than 0 for logarithm and square root.")
    else:
        # Calculate square root
        sqrt_result = math.sqrt(number)

        # Calculate natural logarithm
        log_result = math.log(number)

        # Calculate sine (assuming input is in radians)
        sine_result = math.sin(number)

        # Display the results
        print(f"\nResults for number {number}:")
        print(f"Square root: {sqrt_result}")
        print(f"Natural logarithm (ln): {log_result}")
        print(f"Sine (in radians): {sine_result}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
