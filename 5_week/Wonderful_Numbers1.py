for i in range(10, 100):
    n = i // 10
    c = i % 10
    if 2 * n * c == i:
        print(i)
