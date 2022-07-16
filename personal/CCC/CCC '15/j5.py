# 3d array, where pies is the number of pies, people is the number of people and min is the minimum number of pies for the first person
# its the answer for each and every scenario
visited = []
def pi(pie, people, min):
    if visited[pie][people][min] == 0:
        if pie==people or people ==1:
            visited[pie][people][min] = 1

        else:
            t = 0
            #min is the minimum each person MUST take because of the person infront of them
            for i in range(min, (pie//people)+1): # pie//people is the max the first person can take
                t += pi(pie-i, people-1, i) #t is the total number of ways, in a certain scenario, because it is adjusting the minimum number
                #-i and -1 is to turn into the next turn

            visited[pie][people][min] = t
        return visited[pie][people][min]

pies = int(input())
people = int(input())
for i in range(pies+1):
    x = []
    for y in range(people+1):
        t = []
        for kk in range(pies+1):
            t.append(0)

        x.append(t)
    visited.append(x)

print(pi(pies, people, 1))
