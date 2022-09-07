n = int(input())
a = n//100
b = (n//10)-((n//10)//10) * 10
c = n - (n//10) * 10
print(a + b + c)
