my_list = list(map(int, input().split()))
first_max = my_list[0]
second_max = my_list[0]
first_min = my_list[0]
second_min = my_list[0]
for i in my_list:
    if i >= first_max:
        second_max = first_max
        first_max = i
    elif i >= second_max:
        second_max = i
    if i <= first_min:
        second_min = first_min
        first_min = i
    elif i <= second_min:
        second_min = i
if first_max * second_max > first_min * second_min:
    print(min(first_max, second_max), max(first_max, second_max))
else:
    print(min(first_min, second_min), max(first_min, second_min))
