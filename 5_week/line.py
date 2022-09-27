my_list = list(map(int, input().split()))
high_pety = int(input())
index = 0
for i in my_list:
    if i >= high_pety:
        index += 1

print(index + 1)
