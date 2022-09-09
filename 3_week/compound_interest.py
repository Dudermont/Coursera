p = int(input()) / 100
rub_got = int(input())
cop_got = int(input())
k = int(input())

count = 1
while count <= k:
    cop_have = (rub_got * 100) + cop_got
    cop_have = cop_have + (cop_have * p)
    rub_got = int(cop_have / 100)
    cop_got = int(cop_have % 100)
    count = count + 1

print(rub_got, cop_got)
