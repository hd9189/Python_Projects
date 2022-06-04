n = int(input())
l = [
    1234,
    111,
    123,
    135,
    147,
    159,
    210,
    222,
    234,
    246,
    258,
    321,
    333,
    345,
    357,
    420,
    432,
    444,
    456,
    531,
    543,
    555,
    630,
    642,
    654,
    741,
    753,
    840,
    852,
    951,
    1111
]
def hour(hour):
    if hour == 11:
        return 12
    if hour == 12:
        return 1
    else: return hour + 1

def check(s):
    if len(s)== 4:
        diff1 = int(s[0]) - int(s[1])
        diff2 = int(s[1]) - int(s[2])
        diff3 = int(s[2]) - int(s[3])
        if diff1 == diff2 == diff3:
            return True
        else: return False
    else:
        diff1 = int(s[0]) - int(s[1])
        diff2 = int(s[1]) - int(s[2])
        if diff1 == diff2: return True
        else: return False
h = 12
m = 0
v = 0
for x in range(n+1):
    s = ''
    if m == 59:
        h = hour(h)
        m = 0
        s += str(h)
        s+= '00'
    elif m < 9:
        s+=str(h)
        m +=1
        s += '0' + str(m)
    else:
        m+=1
        s += str(h) + str(m)
    # if check(s):
    #     print(s)
    #     v+=1
# print(v)
    if int(s) in l:
        v+=1

print(v)