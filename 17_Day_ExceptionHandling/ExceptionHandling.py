#Day17: Exception Handling - 30 days of Python learning
'''
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
'''
#1
try: 
    print(10 + '5')
except:
    print('Something went wrong')
#2
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')    # 1970 by default it will take input as a string and will get Type error
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
#3
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)     # here we have type casted the string input into int.
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

#Exercise17.1
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, rs = names
print("nordic_countries: ", nordic_countries)
print("es: ", es)
print("rs: ", rs)


