p = int(input()) / 100
x = int(input()) * 100
y = int(input())

cop_start = x + y
cop_full = cop_start + (cop_start * p)
rub_got = int(cop_full / 100)
cop_got = int(cop_full % 100)

print(rub_got, cop_got)
