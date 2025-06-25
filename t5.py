def factorial(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample number
sample_number = 19

# Call the function and print the output
result = factorial(sample_number)
print(f"The factorial of {sample_number} is: {result}")
