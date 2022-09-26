my_list = list(map(int, input().split()))
n = len(my_list)
second_list = my_list[:]
for i in range(1, n + 1):
    my_list[i - 1] = second_list[n - i]
print(*my_list)
