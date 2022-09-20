my_list = list(map(int, input().split()))
first = my_list[0]
for i in my_list:
    if i > first:
        print(i, end=' ')
    first = i
