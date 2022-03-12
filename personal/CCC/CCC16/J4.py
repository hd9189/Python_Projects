# start = list(input())
# hour = [int(x) for x in start[:2]]
# minute = [int(x) for x in start[3:]]
# start = [hour, minute]
# count = 0 
# rush_hr = [7, 8, 9, 15, 16, 17, 18]

# def rush_hour():
#     global count, start
#     while ((start[0][0]*10 + start[0][1] in rush_hr) and (count < 120)):
#         start[1][0] +=2
#         count += 10
#         if start[1][0] == 6:
#             start[1][0] = 0
#             start[0][1] += 1
#             if start[0][1] ==10:
#                 start[0][1] =0
#                 start[0][0] +=1

# def non_hour():
#     global count, start
#     while ((start[0][0]*10 + start[0][1] not in rush_hr) and (count < 120)):
#         start[1][0] +=1
#         count += 10
#         if start[1][0] == 6:
#             start[1][0] = 0
#             start[0][1] += 1
#         if start[0][1] ==10:
#             start[0][1] =0
#             start[0][0] +=1
#         if start[0][0]*10 + start[0][1] == 24:
#             start[0][0] = 0
#             start[0][1] = 0

# if start[0][0]*10 + start[0][1] in rush_hr:
#     rush_hour()
#     if count < 120:
#         non_hour()

# elif start[0][0]*10 + start[0][1] not in rush_hr:
#     non_hour()
#     if count < 120:
#         rush_hour()
#         if count < 120:
#             non_hour()

# print(f"{start[0][0]}{start[0][1]}:{start[1][0]}{start[1][1]}")

# start = input()
# start = start.split(':')
# start = int(start[0])*60 + int(start[1])
# morning = (7*60, 10*60)
# evening = (15*60, 19*60)

# def rush_hours(end):
#     global count
#     global start
#     min_left = 120 - count
#     #if time will end in rush hour
#     if (start + min_left/2) <= end:
#         start += min_left/2
#         count += min_left
        
#     #if there will still be time after getting out of rush hour
#     elif (start + min_left/2) > end:
#         mins_taken = end - start
#         count += mins_taken*2
#         start += mins_taken

# def normal(startt):
#     global count
#     global start
#     min_left = 120 - count
#     #if not going to enter rush hour
#     if start + min_left <= startt:
#         start += min_left
#         count += min_left
#     #going into rush hour with count that has not yet reached 2 hrs
#     elif start + min_left > startt:
#         min_taken = startt - start
#         count += min_taken
#         start += min_taken

# count = 0

# if start in range(morning):
#     rush_hours(morning[1])
#     normal(evening[0])

# elif start in range(evening):

# else:

start = input().split(":")
time = int(start[0])*60 + int(start[1])
count = 0
morning = (7*60, 10*60)
evening = (15*60, 19*60)

while count < 12:
    if time in range(morning[0], morning[1]) or time in range(evening[0], evening[1]):
        count += 1
        time += 20
    else:
        count += 1
        time += 10

if time >= 1440: time -= 1440

hours = time//60
mins = time - (hours*60)

if hours < 10: hours = "0" + str(hours)
else: hours = str(hours)

if mins < 10: mins = "0" + str(mins)
else: mins = str(mins)

print(hours + ":" + mins)