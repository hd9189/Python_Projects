from __future__ import print_function


first = list(input().replace(" ", ""))
second = list(input().replace(" ",""))

one = set(first)

def hi():
    for x in one:
        if first.count(x) != second.count(x):
            return "Is not an anagram."

    return "Is an anagram."
print(hi())

