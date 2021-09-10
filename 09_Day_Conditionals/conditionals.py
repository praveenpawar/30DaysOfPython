#Day 9: 30 Day of python learning
# ctrl+K+C -> commment for multiple selected line
# ctrl+K+U -> Uncommment for multiple selected line

#Exercise 9.1
age=int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive. Go and learn!!')
else:
    print('you have {} more years to learn to drive.'.format(18-age))

#Exercise 9.2
my_age=26
your_age=int(input('Enter your age: '))
if your_age <= 0:
    print('Please enter the valid age.')
else:
    if my_age > your_age:
        diff=my_age-your_age
        if diff == 1:
            print('you are {} year younger than me.'.format(diff))
        else:
            print('you are {} years younger than me.'.format(diff))
    elif my_age < your_age:
        diff=your_age-my_age
        if diff == 1:
            print('you are {} year older than me.'.format(diff))
        else:
            print('you are {} years older than me.'.format(diff))
    elif my_age == your_age:
        print('We are at same age.')

#Exercise 9.3
num_one = int(input('Enter number one: '))
num_two = int(input('Enter number two: '))
if num_one > num_two:
    print('{} is greater than {}'.format(num_one, num_two))
elif num_one < num_two:
    print('{} is smaller than {}'.format(num_one, num_two))
else:
    print('{} is equal to {}.'.format(num_one, num_two))

#Exercise 9.4
score=int(input('Enter your score: '))
if 80 <= score <= 100:
    print("You have awared with grade: 'A'")
elif 70 <= score <=79:
    print("You have awared with grade: 'B'")
elif 60 <= score <=69:
    print("You have awared with grade: 'C'")
elif 50 <= score <=59:
    print("You have awared with grade: 'D'")
elif 0 <= score <=49:
    print("You have awared with grade: 'F'")
else:
    print('Please enter the valid score.')

#Exercise 9.5
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'Augest']
month=input("Enter the month (Ex. May): ")
if month in Autumn:
    print("The season is Autumn.")
elif month in Winter:
    print("The season is Winter.")
elif month in Spring:
    print("The season is Spring.")
elif month in Summer:
    print("The season is Summer.")
else: print("Enter the valid input")

#Exercise 9.6
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_name = input("Enter the fruit name: ")
if fruit_name in fruits:
    print("That fruit already exist in the fruits list {}".format(fruits))
else:
    fruits.append(fruit_name)
    print("Modified fruits list {}".format(fruits))

#Exercise 9.7
person={
    'first_name': 'Praveen',
    'last_name': 'Pawar',
    'age': 26,
    'country': 'India',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '18th main',
        'zipcode': '562016'
    }
    }
if 'skills' in person.keys():
    mid_skill = person['skills'][2]
    print("Person has 'skills' key in dictionary and middle skill in the skills list is '{}'".format(mid_skill))
    is_python = 'Python' in person['skills']
    print("Person has 'skills' key in dictionary and the person has 'Python' skill: {}".format(is_python))
    print("Person's skill: {}".format(person['skills']))
    if 'JavaScript' and  'React' in person['skills']:
        if 'Node' and 'MongoDB' not in person['skills']:
            print('He is a frontend developer')
    if 'Node' and  'MongoDB' and 'Python' in person['skills']:
        if 'JavaScript' and 'React' not in person['skills']:
            print('He is a backend developer')
    if 'JavaScript' and  'React' and 'Node' and  'MongoDB' and 'Python' in person['skills']:
        print('He is a fullstack developer')
    else: print('unknown title')

# if person['is_married'] == False and person['country'] == 'India': 
#     print("{} {} lives in {} and he is single.".format(person['first_name'], person['last_name'], person['country']))