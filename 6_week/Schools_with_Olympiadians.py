results = open('input.txt', 'r', encoding='utf-8')
schools = [0] * 100
for line in results:
    school = line.split()[2]
    schools[int(school)] += 1
new_list = []
for i in range(len(schools)):
    new_list.append((schools[i], i))
new_list.sort(reverse=True)
third_list = []
a = new_list[0][0]
for i in new_list:
    if i[0] == a:
        third_list.append(i[1])
    else:
        break
third_list.sort()
print(*third_list)
results.close()
