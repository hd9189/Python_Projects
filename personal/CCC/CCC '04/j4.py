word = input()
new=[]
sentence = input()
encryption = {}
for x in sentence: 
    if x.isalpha(): new.append(x)
for x in range(len(word)):
    for y in range(x,len(new), len(word)):
        l = ord(new[y])+(ord(word[x]) - ord('A'))
        if l > 90:
            l-=26
        new[y] = chr(l)
    #encryption[word[x]] = [chr(ord(new[y])+(ord(word[x]) - ord('A')) for y in range(x, len(new), len(word))]
    
print(''.join(new))