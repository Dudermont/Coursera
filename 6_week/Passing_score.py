start_list = open('input.txt', 'r', encoding='utf-8')
end_list = open('output.txt', 'w', encoding='utf-8')
k = int(start_list.readline())
result = []
for line in start_list:
    p1 = int(line.split()[-1])
    p2 = int(line.split()[-2])
    p3 = int(line.split()[-3])
    if p1 >= 40 and p2 >= 40 and p3 >= 40:
        result.append(p1 + p2 + p3)

result.sort(reverse=True)

if len(result) <= k:
    print(0, file=end_list)
else:
    if result[k - 1] == result[k]:
        pass_score = k - 1
        while pass_score > 0 and result[pass_score - 1] == result[pass_score]:
            pass_score -= 1
        if pass_score == 0:
            print(1, file=end_list)
        else:
            print(result[pass_score - 1], file=end_list)
    else:
        print(result[k - 1], file=end_list)

start_list.close()
end_list.close()
