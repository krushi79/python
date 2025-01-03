"""  1: Python Function Arguments """ 
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(5,6)


""" 2: Function Argument with Default Values """

def add_numbers( a = 10,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(4,3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()


"""  3: Python Keyword Argument """
# In keyword arguments, arguments are assigned based on the name of the arguments. 
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'abcd', first_name = 'yures')

"""  4: Python Function With Arbitrary Arguments """

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(9,8,2)

# function call with 2 arguments
find_sum(4, 9)