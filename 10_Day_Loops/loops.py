#Day 10: Loops - 30 days of python learning

#Exercise10.1
count=0
while count < 11:
    print(count)
    count = count + 1

#Exercise10.2
count=10
while count >= 0:
    print(count)
    count = count - 1

#Exercise10.3
for row in range(1, 8):     # Here outer loop is for rows
    for col in range(1, row+1):     # Here inner loop for columns
        print('* ', end='') 
    print()

#Exercise10.4
for row in range(1, 9):     # Here outer loop is for rows
    for col in range(1, 9):     # Here inner loop for columns
        print('* ', end='') 
    print()

#Exercise10.5
count=0
while count < 11:
    print('{} x {} = {}'.format(count, count, count*count))
    count = count + 1

#Exercise10.6
lang = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in lang:
    print(language)

#Exercise10.7 even number
for num in range(0 , 101):
    if num % 2 == 0:
        print(num)

#Exercise10.8 odd number
for num in range(0 , 101):
    if num % 2 != 0:
        print(num)

#Exercise10.9
sum = 0
for num in range(0, 101):
    sum = sum + num

print('The sum of all the numbers is {}'.format(sum))

#Exercise10.10
even_sum = 0
odd_sum = 0
for num in range(0, 101):
    if num % 2 == 0:
        even_sum = even_sum + num
    else: 
        odd_sum = odd_sum + num

print('The sum of all evens is {}. And the sum of all odds is {}.'.format(even_sum, odd_sum))