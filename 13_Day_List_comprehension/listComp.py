#Day 13: List comprehension - 30 days of python programming

#Exercise13.1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive = [i for i in numbers if i > 0]
print(positive)

#Exercise13.2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattned_list = [num for row in list_of_lists for num in row]
print(flattned_list)

#Exercise13.3
numbers = [(i, 1, i, i * i, i * i * i, i * i * i * i, i * i * i * i * i) for i in range(11)]
print(numbers)

#Exercise13.4 # Issue
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattend_list = [(i) for con in countries for i in con]
print(flattend_list)