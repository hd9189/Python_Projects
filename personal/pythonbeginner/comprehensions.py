num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''mylist = []
for n in num:
    mylist.append(n)
print (mylist)
print (mylist[1:-1:2])'''

'''mylist = [n for n in num]
print(mylist)'''

'''mylist = []
for n in num:
   # mylist.append(n*n)
#print(mylist)'''

'''mylist = [n*n for n in num]
print(mylist)'''

#I want 'n' for each 'n' if 'n' is even
'''mylist = []
for n in num:
    if n%2 == 0:
        mylist.append(n)

print(mylist)'''

'''mylist = [n for n in num if n%2 == 0]
print(mylist)'''

'''mylist = []
for letter in 'abcd':
    for num in range(4):
        mylist.append((letter, num))
print (mylist)'''

'''mylist = [(letter, num) for letter in 'abcd' for num in range(4)]
print(mylist)'''

#dictionary comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

'''my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict['Bruce'])
print(my_dict)'''

'''mydict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(mydict)'''

#set comprehensions

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

'''myset = set()
for n in nums:
    myset.add(n)
print(myset)'''

'''myset = {n for n in nums}
print(myset)'''

