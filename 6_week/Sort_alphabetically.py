start_roster = open('input.txt', 'r', encoding='utf8')
end_roster = open('output.txt', 'w', encoding='utf8')
name_list = []
for line in start_roster:
    pupil = [line.split()[0], line.split()[1], line.split()[3]]
    name_list.append(pupil)
name_list.sort()
for pupil in name_list:
    print(' '.join(map(str, pupil)), file=end_roster)
start_roster.close()
end_roster.close()
