lucky_numbers = [4, 15, 8, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1,"Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index(4))

print(friends.count("Toby"))

friends2 = friends.copy()

friends.clear()
print(friends)
