""" 1.Python Global Keyword"""
# global variable
c = 1 
def add():

     # increment c by 2
    c = c + 2

    print(c)

add() 


""" 2: Changing Global Variable From Inside a Function using global"""

# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()


