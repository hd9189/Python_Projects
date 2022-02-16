start = int(input())
end = int(input())
rsa_nums = 0

for number in range(start, end +1):
    divisors = []
    for num in range(1, number +1):
        if number % num == 0:
            divisors.append(num)

    if len(divisors) == 4:
        rsa_nums +=1

print(f"The number of RSA numbers between {start} and {end} is {rsa_nums}")