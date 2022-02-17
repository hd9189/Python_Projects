instructions = input()
instruct = []
numbers = ['1','2','3','4','5','6','7','8','9','0']
indent = 0
for x in range(1,len(instructions)):
    if instructions[x] not in numbers and instructions[x-1] in numbers:
        instruct.append(instructions[indent:x])
        indent = x

instruct.append(instructions[indent:])

for x in instruct:
    if "+" in x:
        index = x.index("+")
        num = x[index+1:]
        print(f"{x[:index]} tighten {int(num)}")
    else:
        index = x.index("-")
        num = x[index+1:]
        print(f"{x[:index]} loosen {int(num)}")