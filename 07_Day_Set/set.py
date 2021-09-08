#Day 7: Set - 30 days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Level1
#Exercise 7.1, 2, 3, 4 ,5
print(it_companies)
print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(['Intel','AMD','Nvidia'])
print(it_companies)
it_companies.remove('twitter')
print(it_companies)
pop_item=it_companies.pop()  # rendomly remove the value
print(pop_item)
print(it_companies)
#Level2
#Exercise 7.1, 2, 3, 4 ,5
print(A)
print(B)
C=A.union(B)
print(C)
D=A.intersection(B)
print(D)
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))
A.update(B)
print(A)
B.update(A)
print(B)
B.symmetric_difference(A)
print(B)
B.clear()
print(B)
del B
print(B)
