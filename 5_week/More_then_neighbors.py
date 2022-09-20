my_list = list(map(int, input().split()))
first = my_list[0]
second = 0
third = 0
count = 0
for i in my_list:
    third = second
    second = first
    first = i
    if third < second and second > first:
        count += 1
print(count)
