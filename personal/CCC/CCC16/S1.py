def thing():
    first = list(input())
    second = list(input())
    copy = first.copy()

    for letter in first:
        if letter in second:
            second.remove(letter)
            copy.remove(letter)


    if len(second) != 0:
        for x in second:
            if x !="*":
                return "N"

    if len(copy) == len(second):
        return "A"
    else:
        return "N"

print(thing())