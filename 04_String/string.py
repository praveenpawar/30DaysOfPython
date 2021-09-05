#Day 4: String - 30 Days of python programming

#Exercise 4.1
first_name='Praveen'
last_name='Pawar'
space=' '
full_name=first_name + space + last_name
print(full_name)

#Exercise 4.2
first_word='Python'
second_word='For'
third_word='All'
print(first_name + space + second_word + space + third_word)

#Exercise 4.3, 4.4, 4.5, 4.6, 4.7, 4.8
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.swapcase())
print(company.capitalize())
print(company.title())

#Exercise 4.9
cut_first=company[:6]
print(cut_first)
#Exercise 4.10
print(company.find('Coding'))
sub_string='Coding'
print(company.index(sub_string))
#Exercise 4.11, 4.12
print(company.replace('Coding', 'Python'))
#Exercise 4.13
print(company.split())
#Exercise 4.14
challenge="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge.split(', '))
#Exercise 4.15
print(company[0])
#Exercise 4.16
print(company[len(company)-1])
#Exercise 4.17
print(company[11])
#Exercise 4.18, 4.19
print(company[0] + company[7] + company[11])
#Exercise 4.20
