'''numbers = []
while True:
    number = input()
    if number == "99999":
        break
    else:
        numbers.append(number)

direction = ""

for number in numbers:
    dir = sum([int(number[0]), int(number[1])])
    steps = int(''.join(number[2:]))
    if ''.join(number[:2]) == "00":
        print(direction, end = " ")
        print(steps)
    elif dir % 2 == 0:
        direction = "right"
        print(direction, end = " ")
        print(steps)
    else:
        direction = "left"
        print(direction, end = " ")
        print(steps)'''

prev = ""
while True:
    instruction = input()
    a = int(instruction[0]) + int(instruction[1])
    if instruction == "9"*5:
        break
    elif a ==0:
        direct = prev
    elif a %2 == 0:
        direct = "right"
    elif a %2 ==1:
        direct = "left"
    print(direct + " " +instruction[2:])
    prev = direct