n = int(input())
result_list = []
for i in range(n):
    name, score = input().split()
    student = (name, int(score))
    result_list.append(student)
result_list.sort(reverse=True, key=lambda x: int(x[1]))
for i in range(len(result_list)):
    print(result_list[i][0])
