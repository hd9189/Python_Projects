x = int(input())
must_in = [input().split() for y in range(x)]

y = int(input())
must_out = [input().split() for x in range(y)]

person = {}
count = 0
for x in range(int(input())):
    group = input().split()
    for y in group: person[y] = count
    count +=1 

violation = 0

for pair in must_in:
    if person[pair[0]] != person[pair[1]]:
        violation +=1

for pair in must_out:
    if person[pair[0]] == person[pair[1]]:
        violation +=1

print(violation)
