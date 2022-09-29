my_list = list(map(int, input().split()))
second_list = my_list[:]
second_list.remove(max(my_list))
second_list.remove(min(my_list))
third_list = second_list[:]
first_max = max(my_list)
second_max = max(second_list)
first_min = min(my_list)
second_min = min(second_list)
if len(my_list) > 3:
    third_list.remove(max(second_list))
    third_max = max(third_list)
if len(my_list) == 3:
    print(*my_list)
elif first_max * second_max * third_max > first_min * second_min * first_max:
    print(first_max, second_max, third_max)
else:
    print(first_min, second_min, first_max)
