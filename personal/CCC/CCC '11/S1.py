sentences = int(input())
t = 0
s = 0
for sentence in range(sentences):
    sen = input().lower()
    t += sen.count("t")
    s += sen.count("s")

if t > s:
    print("English")
else:
    print("French")