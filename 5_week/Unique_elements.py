my_list = list(map(int, input().split()))
second_list = []
for i in my_list:
    if my_list.count(i) == 1:
        second_list.append(i)
print(*second_list)
