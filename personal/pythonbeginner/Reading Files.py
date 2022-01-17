
employee_file = open("Reading Files file", "r")

print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()[2])
print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
