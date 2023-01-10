synonym_dict1, synonym_dict2 = dict(), dict()
for line in range(int(input())):
    words = input().split()
    synonym_dict1[words[0]] = words[1]
    synonym_dict2[words[1]] = words[0]
synonym = input()
if synonym in synonym_dict1:
    print(synonym_dict1[synonym])
else:
    print(synonym_dict2[synonym])
