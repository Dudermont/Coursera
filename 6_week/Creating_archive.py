hdd, n = map(int, input().split())
second_list = []
count = 0
while n != 0:
    second_list.append(int(input()))
    n -= 1
second_list.sort()
for i in second_list:
    if hdd - i >= 0:
        count += 1
        hdd -= i
print(count)
