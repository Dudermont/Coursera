z = int(input())
count = 1
count_max = 1
p = 0

while z != 0:
    if p == z:
        count = count + 1
        if count >= count_max:
            count_max = count
    elif p != z:
        count = 1
    p = z
    z = int(input())

print(count_max)
