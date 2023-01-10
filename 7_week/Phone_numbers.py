def number(s):
    num = []
    for i in s:
        if i.isdigit():
            num.append(int(i))
    if len(num) == 11:
        num = num[1:]
    else:
        num = [495] + num
    return ''.join(map(str, num))


in_file = open('input.txt')
input_number = in_file.readline()
for line in in_file:
    print('YES' if number(line) == number(input_number) else 'NO')
in_file.close()
