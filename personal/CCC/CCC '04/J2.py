start = int(input())
end = int(input())

while True:
    print(f"All positions change in year {start}")
    if start + 60 > end:
        break
    else:
        start += 60