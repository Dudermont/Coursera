class_result = open('input.txt', 'r', encoding='utf-8')
a = []
klass9 = []
klass10 = []
klass11 = []
for line in class_result:
    a += line.split()[2:]
a = [int(i) for i in a]
count = 0
while count != len(a):
    if a[count] == 9:
        klass9.append(a[count + 1])
    elif a[count] == 10:
        klass10.append(a[count + 1])
    elif a[count] == 11:
        klass11.append(a[count + 1])
    count += 2

winners9 = klass9.count(max(klass9))
winners10 = klass10.count(max(klass10))
winners11 = klass11.count(max(klass11))

print(winners9, winners10, winners11)
class_result.close()
