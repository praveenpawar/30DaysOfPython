#Day12 Modules - 30 days of python programming

#Exercise12.1   #generates a six digit/character random_user_id
import string
import random
def random_user_id(length):
    char = string.ascii_lowercase + string.digits
    for i in range(length):
        ran_user_id = random.choice(char)
        print(ran_user_id, end='')
    
random_user_id(6)

#Exercise12.2
import string
import random
length = int(input("Enter the number of the character in user_id: "))
num = int(input("The number of IDs which are supposed to be generated: "))
def random_user_id():
    for i in range(num):
        for j in range(length):
            char = string.ascii_lowercase + string.digits
            ran_user_id = random.choice(char)
            print(ran_user_id, end='')
        print()

random_user_id()