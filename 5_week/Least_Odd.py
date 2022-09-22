my_list = list(map(int, input().split()))
lowodd = 0
for i in my_list:
    if i % 2 > 0 and i != 0:
        odd = i
        if lowodd > odd or lowodd == 0:
            lowodd = odd
print(lowodd)
