# import standard math module 
import math


print("The value of pi is", math.pi)


""" 2. Python import with Renaming """
# import module by renaming it
import math as m

print(m.pi)



"""" Python from...import statement"""
# import only pi from math module
from math import pi

print(pi)



""" Import all names """
from math import *

print("The value of pi is", pi)



""" The dir() built-in function"""
# print(dir(example))




['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']