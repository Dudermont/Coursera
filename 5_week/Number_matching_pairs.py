my_list = list(map(int, input().split()))
count = 0
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            count += 1
print(count)
