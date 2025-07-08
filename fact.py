def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Generate a list containing the Fibonacci series up to n terms."""
    if n <= 0:
        raise ValueError("Number of terms must be a positive integer.")
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer for factorial: "))
        print(f"Factorial of {num} is {factorial(num)}")
        fib_num = int(input("Enter the number of terms for Fibonacci series: "))
        print(f"Fibonacci series with {fib_num} terms: {fibonacci(fib_num)}")
    except ValueError as e:
        print(e)