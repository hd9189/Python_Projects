action = int(input())
time = 0
read = {}
replied = {}
actions = [input().split() for x in range(action)]

for move in actions:
    if move[0] == 'W':
        time += int(move[1])-1
    
    elif move[0] == 'R':
        read[move[1]] = time
        time +=1

    elif move[0] == "S":
        if int(move[1]) not in replied.keys():
            replied[int(move[1])] = time - read[move[1]]
        else:
            replied[int(move[1])] += time - read[move[1]]

        read.pop(move[1])

        time +=1

for act in read.keys():
    replied[int(act)] = -1

result = {}
keys = list(replied.keys())
keys.sort()

for key in keys:
    result[key] = replied[key]

for person, time in result.items():
    print(person, end = " ")
    print(time)
