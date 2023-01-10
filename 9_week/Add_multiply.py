from sys import stdin


class MatrixError(Exception):
    def __init__(self, obj, other):
        self.matrix1 = obj
        self.matrix2 = other


class Matrix:
    @staticmethod
    def transposed(obj):
        return Matrix([[obj.rlist[j][i] for j in range(len(obj.rlist))]
                       for i in range(len(obj.rlist[0]))])

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

    def __add__(self, other):
        if len(self.rlist) == len(other.rlist):
            ri, rj = range(len(self.rlist)), range(len(self.rlist[0]))
            return Matrix([[self.rlist[i][j] + other.rlist[i][j] for j in rj]
                           for i in ri])
        else:
            raise MatrixError(self, other)

    def __mul__(self, skal):
        ri, rj = range(len(self.rlist)), range(len(self.rlist[0]))
        return Matrix([[self.rlist[i][j] * skal for j in rj] for i in ri])

    __rmul__ = __mul__

    def transpose(self):
        self.rlist = [[self.rlist[j][i] for j in range(len(self.rlist))]
                      for i in range(len(self.rlist[0]))]
        return Matrix(self.rlist)


exec(stdin.read())
