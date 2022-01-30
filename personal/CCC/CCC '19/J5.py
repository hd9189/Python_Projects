a = int(input())
st = []
for x in range(a):
    st.append(input())

for y in range(a):
    n = st[y]
    s = ""
    count = 0
    for l in range(len(n)):
        if l != len(n) -1 and n[l] == n[l+1]:
            count +=1
        else:
            s += " " + str(count+1)+" " + n[l]
            count = 0
    print(s[1:len(s)])
