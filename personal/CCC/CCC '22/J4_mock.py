num = input().split()
num = [int(x) for x in num]
people = input().split()
students = [[int(x)] for x in people]
last_hit = []

for rounds in range(num[1]):
    #last round
    if rounds == num[1]-1:
        for student in range(len(students)):
            if len(students[student]) == 0:
                last_hit.append(1)
            else:
                last_hit.append(students[student][0])

    else:
        for student in range(len(students)):
            if len(students[student]) == 0:
                continue
            else:
                #person hit with a -1 cuz of index
                hit = students[student][0]-1
                #plus one cuz of indexing
                students[hit].append(student+1)
                students[student].pop(0)

for hit in range(len(last_hit)):
    if hit == len(last_hit)-1:
        print(last_hit[hit])
    else:
        print(last_hit[hit], end = " ")