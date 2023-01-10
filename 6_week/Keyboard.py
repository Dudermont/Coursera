keys = int(input())
strength = list(map(int, input().split()[:keys]))
score_pressing = int(input())
pressing = list(map(int, input().split()[:score_pressing]))

for i in pressing:
    strength[i - 1] -= 1

for i in strength:
    if i < 0:
        print("YES")
    else:
        print("NO")
