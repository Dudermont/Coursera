start_roaster = open('input.txt', 'r', encoding='utf-8')
n, m = map(int, start_roaster.readline().split())
cub_ana = set()
cub_bor = set()
while len(cub_ana) < n:
    cub_ana.add(int(start_roaster.readline()))
while len(cub_bor) < m:
    cub_bor.add(int(start_roaster.readline()))
print(len(cub_ana & cub_bor))
print(*sorted(cub_ana & cub_bor))
print(len(cub_ana - cub_bor))
print(*sorted(cub_ana - cub_bor))
print(len(cub_bor - cub_ana))
print(*sorted(cub_bor - cub_ana))
