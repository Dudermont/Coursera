def merge(A, B):
    C = []
    n = 0
    i = 0
    while n < len(A) and i < len(B):
        if A[n] <= B[i]:
            C.append(A[n])
            n += 1
        else:
            C.append(B[i])
            i += 1
    if n < len(A):
        C.extend(A[n:])
    else:
        C.extend(B[i:])
    return C


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

print(*merge(first_list, second_list))
