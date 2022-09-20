n = int(input())
summ1 = 0
summ = (n * (n + 1)) // 2
for i in range(n - 1):
    k = int(input())
    summ1 += k

lostcard = summ - summ1
print(lostcard)
