my_list = list(map(int, input().split()))
index = 0
high = 0

for i in my_list:
    if i >= high:
        high = i
        highindex = index
    index += 1

print(high, highindex)
