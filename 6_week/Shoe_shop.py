n = int(input()) - 3
first_list = sorted(map(int, input().split()))
count = 0
for i in first_list:
    if n <= i - 3:
        n = i
        count += 1
print(count)
