results = open('input.txt', 'r', encoding='utf-8')
new_list = []
for line in results:
    new_list.append((int(line.split()[2]), int(line.split()[3])))
results.close()
new_list.sort()

klass9, klass10, klass11 = [], [], []
for i in new_list:
    if i[0] == 9:
        klass9.append(i[1])
    elif i[0] == 10:
        klass10.append(i[1])
    else:
        klass11.append(i[1])
klass9.sort(reverse=True)
klass10.sort(reverse=True)
klass11.sort(reverse=True)

final_list = []

k9max = klass9[0]
for i in klass9:
    if i == k9max:
        continue
    else:
        final_list.append(i)
        break

k10max = klass10[0]
for i in klass10:
    if i == k10max:
        continue
    else:
        final_list.append(i)
        break
k11max = klass11[0]
for i in klass11:
    if i == k11max:
        continue
    else:
        final_list.append(i)
        break
print(*final_list)
