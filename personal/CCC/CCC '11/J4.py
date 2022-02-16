#unfinished
location = [-1,-5]
coordinates = []
a = location.copy()
coordinates.append(a)

while True:
    direction = input().split()
    if direction[0] == "q":
        break
    else:

        if direction[0] == "d": 
            location[1] -= int(direction[1])
        elif direction[0] == "u": 
            location[1] += int(direction[1])
        elif direction[0] == "l": 
            location[0] -= int(direction[1])
        elif direction[0][0] == "r": 
            location[0] += int(direction[1])
        b = location.copy()

        if location in coordinates:
            print(f"{location[0]} {location[1]} DANGER")
            break
        if (location[0] < (-3)) or (location[0] > 10) or (location[1] > (-1)) or (location[1] < (-8)):
            print(f"{location[0]} {location[1]} DANGER")
            break
        else:
            print(f"{location[0]} {location[1]} safe")
            coordinates.append(b)