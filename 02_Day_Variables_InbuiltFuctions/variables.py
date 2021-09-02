#Day 2: Variables and Inbuilt fuction - 30 days of python programming

#Exercise: Level1
first_name="Praveen"
last_name="Pawar"
full_name="Praveen Pawar"
country="India"
city="Bengaluru"
age=26
year=2021
is_married="No"
is_true=True
is_light_ON=False
name, age, mobile="praveen", 26, 8109

#Exercise: Level2.1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_ON))

#Exercise: Level2.2
print(len(first_name))
#Exercise: Level2.3
print(bool(len(first_name)==len(last_name)))
#Exercise: Level2.4
num_one=5
num_two=4
total=int(num_one + num_two)
print(total)
diff=int(num_one - num_two)
print(diff)
product=int(num_one * num_two)
print(product)
devide=int(num_one / num_two)
print(devide)
reaminder=int(num_one % num_two)
print(reaminder)
exp=int(num_one ** num_two)
print(exp)
floor_devision=int(num_one // num_two)
print(floor_devision)
#Exercise: Level2.5
radius=30
area_of_circle=3.14 * (30 ** 2)
print('area of circle: ', area_of_circle)
circum_of_circle=2 * 3.14 * 30
print('circum of circle: ', circum_of_circle)
User_radius=int(input(('radius_of_circle: ')))
User_area=3.14 * (User_radius ** 2)
print('area of circle: ', User_area)

#Exercise: Level2.6
fName=input('Enter your first name : ')
lName=input('Enter your last name: ')
Age=input('Enter your age : ')
Country=input('Enter your country name: ')
User_list=[fName, lName, Age, Country]
print('User details: ', User_list)


