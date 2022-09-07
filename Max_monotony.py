n1 = n2 = n3 = int(input())
count = 1
count_max = 0

while n1 != 0:
    if n1 > n2 > n3 or n1 < n2 < n3:
        count = count + 1
    elif n1 < n2 or n1 > n2:
        count = 2
    if count > count_max:
        count_max = count
    n3 = n2
    n2 = n1
    n1 = int(input())

print(count_max)
