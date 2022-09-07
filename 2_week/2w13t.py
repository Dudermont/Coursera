a = int(input())
b = int(input())
c = int(input())

a1 = a ** 2
b1 = b ** 2
c1 = c ** 2
k1 = (a1 + c1 - b1)
j1 = (a1 + b1 - c1)
w1 = (b1 + c1 - a1)
k2 = a * c * 2
j2 = a * b * 2
w2 = b * c * 2

k = k1 / k2
j = j1 / j2
w = w1 / w2

t = k % 2
y = j % 2
u = w % 2

if -1 < k < 1 or -1 < j < 1 or -1 < w < 1:
    if k == 0 or w == 0 or j == 0:
        print('rectangular')
    elif k < 0 or j < 0 or w < 0:
        print('obtuse')
    else:
        print('acute')
else:
    print('impossible')
