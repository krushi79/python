""" Python Recursion """

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 6
print("The factorial of", num, "is", factorial(num))


