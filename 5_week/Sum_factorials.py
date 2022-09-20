n = int(input())
summ = 0
for i in range(1, n + 1):
    count = 1
    while i != 1:
        count *= i
        i -= 1
    summ += count
print(summ)
