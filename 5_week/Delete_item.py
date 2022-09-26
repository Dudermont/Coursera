my_list = list(map(int, input().split()))
k = int(input())
n = len(my_list)
for i in range(k, n - 1):
    my_list[i] = my_list[i + 1]
my_list.pop()
print(*my_list)
