my_list = list(map(int, input().split()))
count = 0
prev = my_list[0]
for i in my_list:
    if i > prev:
        count += 1
        prev = i
print(count + 1)
