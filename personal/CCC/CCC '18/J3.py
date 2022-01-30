dis = input().split()
distance = [int(x) for x in dis]
for x in range(len(distance)+1):
    distance.insert(x,0)
    d = []
    count = 0
    for y in distance[x::-1]:
        count +=y
        d.insert(0,count)
    count = 0
    for y in distance[x+1:]:
        count +=y
        d.append(count)
    answer = ' '.join([str(x) for x in d])
    print(answer)
    distance.pop(x)