import sys

sys.setrecursionlimit(3000)

i = 0

def greet():
    global i
    i += 1
    print("HELLO", i)
    greet()


greet()