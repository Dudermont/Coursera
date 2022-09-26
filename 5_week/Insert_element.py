my_list = list(map(int, input().split()))
k, c = map(int, input().split())
my_list.append(c)
n = len(my_list)
for i in range(n - 1, k, -1):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
print(*my_list)
