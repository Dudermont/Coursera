in_file = open('input.txt')
word_dict = {}
for line in in_file:
    words = line.split()
    for elem in words:
        word_dict[elem] = word_dict.get(elem, 0) + 1

print(max(sorted(word_dict), key=word_dict.get))
in_file.close()
