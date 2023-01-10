from sys import stdin


class Matrix:
    def __init__(self, rlist):
        self.rlist = []
        for i in range(len(rlist)):
            self.rlist.append(rlist[i][:])

    def __str__(self):
        strings = ''
        for elem in self.rlist:
            string = '\t'.join([str(i) for i in elem])
            strings += string + '\n'
        return strings[:-1]

    def size(self):
        return len(self.rlist), len(self.rlist[0])


exec(stdin.read())
