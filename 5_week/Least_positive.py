my_list = list(map(int, input().split()))
start = my_list[0]
if start > 0:
    lowest = start
else:
    lowest = 1000
for i in my_list:
    if 0 < i < lowest:
        lowest = i
print(lowest)
