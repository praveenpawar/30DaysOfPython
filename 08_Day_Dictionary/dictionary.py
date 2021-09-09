#Day 8: Dictionay - 30 Days of Python programming

#Exercise8.1
dct = dict()
print(dct)
#Exercise8.2, 3, 4, 5, 6
student = {
    'first_name':'Praveen',
    'last_name':'Pawar',
    'age':120,
    'country':'India',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'18th Main road',
        'zipcode':'562016'
    }
    }
print(student)
print(student['country'])
#print(student['city']) # will get key error here, use get method to avoid unassiged key access
print(student.get('city'))
student['city'] = 'Bengaluru'
student['skills'].append('HTML')
print(student)

print(len(student))
print(student['skills'])
print(type(student['skills']))

#Exercise8.7, 8
keys=student.keys()
print(keys)
values=student.values()
print(values)

#Exercise8.9
print(student.items())
#Exercise8.10
del student['is_married']
student.pop('address')
print(student)
student.pop('skills')
print(student)
student.popitem()
print(student)
#Exercise8.10
del student
print(student)