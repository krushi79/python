""" 1. Python Local Variables """

def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()



""" 2. Python Global Variables"""


message = 'Hello'

def greet():

    print('Local', message)

greet()
print('Global', message)



