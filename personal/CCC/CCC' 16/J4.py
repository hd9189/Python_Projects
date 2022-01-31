#unfinished
start = list(input())
start.remove(":")
start_a = [int(x) for x in start]
start_a[0] = [start_a[0]*10, start_a[1]]
start_a.pop(1)
start_a[1] = [start_a[1]*10, start_a[2]]
start_a.pop(2)

count = 0
while count <200:
    while start_a[1][0] != 0:
        if sum(start_a[0]) in range(7,11) or sum(start_a[0]) in range(5,20):
            count += 10
            start_a[1][0] += 20
            if start_a[1][0] == 60:
                start_a[1][0] =0
                start_a[0][1] += 1
                if start_a[0][1] == 10:
                    start_a[0][1] =0
                    start_a[0][0] +=1

        if sum(start_a[0]) not in range(7,11) or sum(start_a[0]) not in range(5,20):
            count += 10
            start_a[1][0] += 10
            if start_a[1][0] == 60:
                start_a[1][0] =0
                start_a[0][1] += 1
                if start_a[0][1] == 10:
                    start_a[0][1] =0
                    start_a[0][0] +=1
print(start_a)
    