#Day 3: Operators - 30 days of python programming

#Exercise 3.1, 3.2, 3.3
age=26
print(int(age), 'year old')
height=177.5
print(float(height), 'cms')
com_num=2+3j
print(type(com_num))

#Exercise 3.4       #Area of the triangle
Tri_base=int(input('Enter the base of triangle: '))
Tri_height=int(input('Enter the height of triangle: '))
Tri_area=int(0.5 * Tri_base * Tri_height)
print('Area of the triangle is ', Tri_area)

#Exercise 3.5       #perimeter of the triangle
side_a=int(input('Enter side a: '))
side_b=int(input('Enter side b: '))
side_c=int(input('Enter side c: '))
perimeter=int(side_a+side_b+side_c)
print('perimeter of the triangle is ', perimeter)

#Exercise 3.6       #Area and perimeter of a rectangle
length=int(input('Enter a length: '))
width=int(input('Enter a width: '))
Rec_area=int(length*width)
Rec_perimeter=int(2*(length+width))
print('Area of a rectangle is ', str(Rec_area) + ' and Perimeter of a rectangle is ', str(Rec_perimeter))