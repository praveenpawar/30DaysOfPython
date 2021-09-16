#Day14 HOF - 30 days of python learning

#Exercise14.1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''syntax map(function, iterable)
'''
#Exp: map1
def upper_case(name):
    return name.upper()

names_upper_cased = map(upper_case, names)
print(list(names_upper_cased))
#this example using lambda fuction
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

#Exp: map2
squared_values = map(lambda x: x*x, numbers)
print(list(squared_values))

'''syntax filter(function, iterable)
'''
#Exp: filter1
def longer_value(name):
    return len(name)>6

longer_value_name = filter(longer_value, countries)
print(list(longer_value_name))
# this example with lambda function
longer_value_name = filter(lambda name: len(name)>6, countries)
print(list(longer_value_name))

#Exp: filter2
def even_value(x):
    if x % 2 == 0:
        return True
    return False

even_value_number = filter(even_value, numbers)
print(list(even_value_number))

'''syntax reduce(function, iterable)
   it does not return another iterable, instead it returns a single value.
   this fuction is part of functools module.
'''

# Exp: reduce
import functools as ft
def add_two_num(x, y):
    return x+y

total = ft.reduce(add_two_num, numbers)
print(total)