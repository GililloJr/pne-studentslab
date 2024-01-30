def fibon(n):
    if n <= 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)

# Main program
fibonacci_5th = fibon(5)
fibonacci_10th = fibon(10)
fibonacci_15th = fibon(15)

print(f"The 5th Fibonacci term is: {fibonacci_5th}")
print(f"The 10th Fibonacci term is: {fibonacci_10th}")
print(f"The 15th Fibonacci term is: {fibonacci_15th}")



