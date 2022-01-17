a = 10
b = 11
c = 12

def something():
    global a
    a = 5
    print(a, "in function")

something()

print(a,"out function")

def somethingelse():
    b = 21
    globals()['b'] = 20

    print(b, "in function")

somethingelse()

print(b,"out function")