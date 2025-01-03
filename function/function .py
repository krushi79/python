""" 1. Create a function"""
def greet():
    print('Hello World!')
# call the function
greet()
print('Hello world')



""" 2. Python Function Call """

def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')


"""  3 Python Function Arguments """

def greet(name):
    print("Hello", name)
# pass argument
greet("krushi")


""" 4. Function to Add Two Numbers """

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(9,6)

""""5. Parameter vs Arguments"""

def print_age(age):  
    print(age)

print_age(30)  


"""6. Pass statement"""

def future_function():
    pass

# this will execute without any action or error
future_function()  


""" 7. Python Library Function """
import math

square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)


power = pow(3,4)

print("3 to the power 4 is",power)


"""8. Default Arguments in Functions """


def greet(name, message="Hello"):
    print(message, name)

greet("Alice", "Good Morning")
greet("Bob")

"""9. Using *args and **kwargs in Functions """


def add_all(*numbers):
    return sum(numbers)
print(add_all(1, 2, 3, 4,5))   


#10. Using **kwargs allows the function to accept any number of keyword arguments.

# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")


greet(name="krushi", greeting="Hello")