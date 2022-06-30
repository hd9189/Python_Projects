# n = int(input())

# def hour(hour):
#     if hour == 11:
#         return 12
#     if hour == 12:
#         return 1
#     else: return hour + 1

# def check(s):
#     if len(s)== 4:
#         diff1 = int(s[0]) - int(s[1])
#         diff2 = int(s[1]) - int(s[2])
#         diff3 = int(s[2]) - int(s[3])
#         if diff1 == diff2 == diff3:
#             return True
#         else: return False
#     else:
#         diff1 = int(s[0]) - int(s[1])
#         diff2 = int(s[1]) - int(s[2])
#         if diff1 == diff2: return True
#         else: return False
# h = 12
# m = 0
# v = 0
# for x in range(n+1):
#     s = ''
#     if m == 59:
#         h = hour(h)
#         m = 0
#         s += str(h)
#         s+= '00'
#     elif m < 9:
#         s+=str(h)
#         m +=1
#         s += '0' + str(m)
#     else:
#         m+=1
#         s += str(h) + str(m)
#     if check(s):
#         print(s)
#         v+=1
# print(v)

day_c = 31
h_c = 720

d = int(input())
h = 12
m = 0
cnt = 0
#runs only if there is remaining hours
for i in range(d % h_c):
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 13:
        h = 1
    #creates a string of the number with :
    clock = str(h) + '%02d' % m
    dif = int(clock[1]) - int(clock[0])
    for j in range(1, len(clock)):
        if int(clock[j]) - int(clock[j - 1]) != dif:
            #breaks out of for loop and immedietly goes back up to the top
            break
    #prints 
    else:
        cnt += 1
#cnt: counts for the remaining minutes, if the input is over 720 mins (12 hours)
#day_c*(d//h_c) is sum of how many sames there are for every 720 mins
print(cnt + day_c * (d // h_c))