nums = [10,12,14,16,18,20]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")