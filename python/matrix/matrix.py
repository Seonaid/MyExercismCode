class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = matrix_string.splitlines()
        self.rows = [[int(i) for i in line.split()] for line in self.rows]
        self.columns = [list(a) for a in list(zip(*self.rows))]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
