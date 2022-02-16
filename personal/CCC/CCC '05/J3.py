#not finished
places = []
direction = ''
street = ''
while street != "SCHOOL":
    direction = input()
    street = input()
    places.append([direction, street])

a = places[:-1]

for thing in a[::-1]:
    if thing[0] == "R":
        dir = "LEFT"
    elif thing[0] == "L":
        dir = "RIGHT"
    print(f"Turn {dir} onto {thing[1]} street.")

if places[-1][0] == "R":
        dir = "LEFT"
elif places[-1][0] == "L":
    dir = "RIGHT"

print(f"Turn {dir} into your HOME.")