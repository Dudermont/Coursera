my_list = list(map(int, input().split()))
min = my_list[0]
max = my_list[0]
for i in my_list:
    if i > max:
        max = i
    if i < min:
        min = i
index_min = my_list.index(min)
index_max = my_list.index(max)
my_list.pop(index_max)
my_list.insert(index_max, min)
my_list.pop(index_min)
my_list.insert(index_min, max)
print(*my_list)
