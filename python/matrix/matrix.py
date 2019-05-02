class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [x.split(' ') for x in matrix_string.split('\n')]

    def row(self, index):
        return [int(x) for x in self.matrix[index-1]]

    def column(self, index):
        return [int(r[index-1]) for r in self.matrix]