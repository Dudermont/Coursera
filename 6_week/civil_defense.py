def shelters_find(a, b):
    d = abs(villages[a][0] - shelters[b][0])
    while b < len(shelters) - 1:
        if abs(villages[a][0] - shelters[b + 1][0]) >= d:
            return b
        else:
            d = abs(villages[a][0] - shelters[b + 1][0])
            b += 1
    return b


n = int(input())
z = list(map(int, input().split()))
villages = []
for i in range(len(z)):
    villages.append((int(z[i]), i + 1))
villages.sort()

m = int(input())
r = list(map(int, input().split()))
shelters = []
for i in range(len(r)):
    shelters.append((int(r[i]), i + 1))
shelters.sort()
shelters_villages_list = []
a, b = 0, 0
while a < len(villages):
    b = shelters_find(a, b)
    shelters_villages_list.append((villages[a][1], shelters[b][1]))
    a += 1
shelters_villages_list.sort()
i = 0
while i < len(shelters_villages_list):
    print(shelters_villages_list[i][1], end=' ')
    i += 1
