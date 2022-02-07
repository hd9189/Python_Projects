start = list(input())
hour = [int(x) for x in start[:2]]
minute = [int(x) for x in start[3:]]
start = [hour, minute]
count = 0 
rush_hr = [7, 8, 9, 15, 16, 17, 18]

def rush_hour():
    global count, start
    while ((start[0][0]*10 + start[0][1] in rush_hr) and (count < 120)):
        start[1][0] +=2
        count += 10
        if start[1][0] == 6:
            start[1][0] == 0
            start[0][1] += 1
            if start[0][1] ==10:
                start[0][1] ==0
                start[0][0] +=1

def non_hour():
    global count, start
    while ((start[0][0]*10 + start[0][1] not in rush_hr) and (count < 120)):
        start[1][0] +=1
        count += 10
        if start[1][0] == 6:
            start[1][0] == 0
            start[0][1] += 1
            if start[0][1] ==10:
                start[0][1] ==0
                start[0][0] +=1
            if start[0][0]*10 + start[0][1] == 24:
                start[0][0] = 0
                start[0][1] = 0

if start[0][0]*10 + start[0][1] in rush_hr:
    rush_hour()
    if count < 120:
        non_hour()

elif start[0][0]*10 + start[0][1] not in rush_hr:
    non_hour()
    if count < 120:
        rush_hour()

print(f"{start[0][0]}{start[0][1]}:{start[1][0]}{0}")
