def CountSort(A):
    dop_list = [0] * 101
    for now in A:
        dop_list[now] += 1
    for now in range(len(A)):
        A.pop()
    for now in range(101):
        for i in range(dop_list[now]):
            A.append(str(now))
    return A


start_list = list(map(int, input().split()))
CountSort(start_list)
print(*start_list)
