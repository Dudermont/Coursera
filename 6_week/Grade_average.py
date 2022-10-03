educ_room = open('input.txt', 'r', encoding='utf8')
points_9 = []
points_10 = []
points_11 = []
pupils_9 = 0
pupils_10 = 0
pupils_11 = 0
pupils_points = []
for line in educ_room:
    pupils_points += line.split()[2:]
pupils_points = [int(i) for i in pupils_points]
i = 0
while i != len(pupils_points):
    if pupils_points[i] == 9:
        points_9.append(pupils_points[i + 1])
        pupils_9 += 1
    elif pupils_points[i] == 10:
        points_10.append(pupils_points[i + 1])
        pupils_10 += 1
    elif pupils_points[i] == 11:
        points_11.append(pupils_points[i + 1])
        pupils_11 += 1
    i += 2
print(sum(points_9) / pupils_9, sum(points_10) / pupils_10,
      sum(points_11) / pupils_11)
educ_room.close()
