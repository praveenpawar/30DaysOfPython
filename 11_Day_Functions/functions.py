#Day 11: Functions - 30 days of python programming 

#Exercise11.1
def add_two_numbers(num_one, num_two):
    sum = 0
    sum = num_one + num_two
    return sum

print(add_two_numbers(5, 6))

#Exercise11.2
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area

print(area_of_circle(2))

#Exercise11.3
def add_all_nums(*nums):    #take arbitrary number of arguments as tuple
    sum = 0
    for num in nums:
        sum += num  # same as total = total + num 
    return sum

print(add_all_nums(2 , 3, 5))

#Exercise11.4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = 0
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(37))

#Exercise11.5
def check_season(month):
    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'Augest']
    
    if month in Autumn:
        print("The season is Autumn.")
    elif month in Winter:
        print("The season is Winter.")
    elif month in Spring:
        print("The season is Spring.")
    elif month in Summer:
        print("The season is Summer.")
    else: print("Enter the valid input")

print(check_season('May'))

#Exercise11.6
#Exercise11.7
#Exercise11.8
def print_list(lst):
    i = 0
    for i in range(len(lst)):
        print(lst[i])
    
print(print_list([1, 2, 3, 4, 5]))

#Exercise11.9 
def reverse_list(lst):
    rev_lst = []
    for i in range(len(lst)-1, -1, -1):
        rev_lst.append(lst[i])
    return rev_lst

print(reverse_list([1, 2, 3, 4, 5]))

#Exercise L2.1
def evens_and_odds(num):
    odd=0; even=0
    for i in range(num+1):
        if i % 2 == 0:
            even+=1
        else: odd+=1
    return even, odd

num=int(input("Enter the value: "))
result=evens_and_odds(num)
print("The number of even: ", result[0])
print("The number of odd: ", result[1])
