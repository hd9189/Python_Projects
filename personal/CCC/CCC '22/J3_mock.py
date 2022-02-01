#????
a = [int(x) for x in input().split()]
first = list(input())
second = list(input())
count = 0
first_letter = ''
second_letter = ''
first_count = 0
second_count = 0



for word in range(a[0]):
    if first[word] not in second:
        if first.count(first[word]) > first_count:
            first_letter = first[word]
            first_count = first.count(first[word])
            continue
        else: continue

    for letter in range(a[1]):
        if second[letter] not in first:
            if second.count(second[letter]) > second_count:
                second_letter = second[letter]
                second_count = second.count(second[letter])
                continue
            else: continue

        if first[word] == second[letter]:
            count += 1

if second_count > first_count:
    print(count + second_count)
else: print(count+ first_count)