in_file = open('input.txt')
country_city = dict()
for i in range(int(in_file.readline())):
    a = in_file.readline().split()
    country_city[a[0]] = set(a[1:])

for i in range(int(in_file.readline())):
    question = in_file.readline().strip()
    print(*[country for country in country_city
            if question in country_city[country]])
in_file.close()
