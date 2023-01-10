olimpic_result = open('input.txt', 'r', encoding='utf-8')
result9 = []
result10 = []
result11 = []
for line in olimpic_result:
    if int(line.split()[2]) == 9:
        puple = (int(line.split()[3]))
        result9.append(puple)
    if int(line.split()[2]) == 10:
        puple = (int(line.split()[3]))
        result10.append(puple)
    if int(line.split()[2]) == 11:
        puple = (int(line.split()[3]))
        result11.append(puple)
result9.sort()
result10.sort()
result11.sort()
print(max(result9), max(result10), max(result11))
olimpic_result.close()
