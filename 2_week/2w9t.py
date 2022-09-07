n = int(input())

r = n - (n//10) * 10

if r == 1:
    if n == 11:
        print(n, 'korov')
    else:
        print(n, 'korova')
elif 10 < n < 20 or r == 0 or r == 5 or r == 6 or r == 7 or r == 8 or r == 9:
    print(n, 'korov')
else:
    print(n, 'korovy')
