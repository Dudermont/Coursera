n = int(input())
my_list1 = list(map(int, input().split()))
my_list = my_list1[0:n]
x = int(input())
index = my_list[0]
for i in my_list:
    if abs(i - x) < abs(x - index):
        index = i
print(index)
