my_list = list(map(int, input().split()))
first = 0
before = 0
for i in my_list:
    if i > 0:
        before = first
        first = i
        if before > 0 and first > 0:
            print(before, first)
            break
    elif i < 0:
        before = first
        first = i
        if before < 0 and first < 0:
            print(before, first)
            break
    first = i
