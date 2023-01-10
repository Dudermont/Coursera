kilometer = list(map(int, input().split()))
tax = list(map(int, input().split()))
kilometer.sort()
tax.sort(reverse=True)
cost = 0
for i in range(len(kilometer)):
    cost += kilometer[i] * tax[i]
print(cost)
