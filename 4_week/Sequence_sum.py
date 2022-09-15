def seq_sum(n):
    if n == 0:
        return n
    return n + seq_sum(n=int(input()))


n = int(input())
print(seq_sum(n))
