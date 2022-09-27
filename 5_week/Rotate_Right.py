my_list = list(map(int, input().split()))
n = len(my_list)
listName = []
listName.append(my_list[n - 1])
i = 0
while i < n - 1:
    listName.append(my_list[i])
    i += 1
print(*listName)
