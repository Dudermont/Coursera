my_list = list(map(int, input().split()))
n = len(my_list)
second_list = []
i = 0
if n % 2 != 0:
    while i < n - 1:
        second_list.append(my_list[i + 1])
        second_list.append(my_list[i])
        i += 2
    second_list.append(my_list[n - 1])
else:
    while i < n:
        second_list.append(my_list[i + 1])
        second_list.append(my_list[i])
        i += 2
print(*second_list)
