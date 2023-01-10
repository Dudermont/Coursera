n = list(map(int, input().split()))
first_route, second_route = [], []
for i in range(len(n)):
    if i < 2:
        first_route.append(n[i])
    else:
        second_route.append(n[i])
first_route.sort()
second_route.sort()
first_bus = set(range(first_route[0], first_route[1] + 1))
second_bus = set(range(second_route[0], second_route[1] + 1))

print(len(first_bus & second_bus))
