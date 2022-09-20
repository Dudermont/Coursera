def IsAscending(A):
    g = len(A) - 1
    index = 0
    while A[g] > A[g - 1]:
        index += 1
        g -= 1
    return index


my_list = list(map(int, input().split()))

if IsAscending(my_list) == len(my_list) - 1:
    print('YES')
else:
    print('NO')
