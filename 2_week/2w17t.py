A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if E >= A and (D >= B or D >= C):
    print('YES')
elif E >= B and (D >= A or D >= C):
    print('YES')
elif E >= C and (D >= B or D >= A):
    print('YES')
else:
    print('NO')
