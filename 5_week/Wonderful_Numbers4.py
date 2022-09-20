a = int(input())
b = int(input())

for i in range(a, b + 1):
    first = i // 1000
    second = (i % 1000) // 100
    third = ((i % 1000) % 100) // 10
    last = ((i % 1000) % 100) % 10
    if first == last and second == third:
        print(i)
