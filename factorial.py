# factorial.py - a function that returns the value of factorial

def factorial(n):
    if n == 1:
        result = 1
    elif n >= 2:
        result = n * factorial(n - 1)
    return result

print factorial(4)
