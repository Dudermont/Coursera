n = int(input())
first_list = list(map(int, input().split()))
second_list = first_list[:n]
print(*sorted(second_list))
