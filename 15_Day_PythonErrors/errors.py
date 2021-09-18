#Day15: Types of Error - 30 days of python programming

##Syntax error
#print 'Hello World'

'''print 'Hello World'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello World')?'''

#print('Hello world')

##Name error
#print(age)

'''print(age)
NameError: name 'age' is not defined'''

# age = 18
# print(age)

##Index error
# numbers = [1, 2, 3, 4, 5]
# print(numbers[5])

'''print(numbers[5])
IndexError: list index out of range'''

# print(numbers[4])

##ModuleNotFoundError
#import maths

'''import maths
ModuleNotFoundError: No module named 'maths'.'''

#import math

##Atribute error
#import math
#print(math.PI)

'''print(math.PI)
AttributeError: module 'math' has no attribute 'PI'.'''

#print(math.pi)

##Key error
# users = {'name':'Praveen', 'age':26, 'country':'India'}
# print(users['county'])

'''print(users['county'])
KeyError: 'county'.'''

#print(users['country'])

##Type error
#print(2 + '3')

'''print(2 + '3')
TypeError: unsupported operand type(s) for +: 'int' and 'str'.'''

#print(2 + 3)

##Import error
#from math import power

'''from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)'''

# from math import pow
# print(pow(2,3))

##Value error
#int('12a')

'''int('12a')
ValueError: invalid literal for int() with base 10: '12a'.'''

##ZeroDivisionError
#print(1/0)

'''print(1/0)
ZeroDivisionError: division by zero.'''
