def factorial(n):
    if n == 1:               # base case
        return 1
    else:
        return n * factorial(n - 1)   # recursive call

# test
num = 5
print(f"Factorial of {num} is:", factorial(num))
