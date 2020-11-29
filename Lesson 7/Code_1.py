class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ""
        b = ""
        for row in self.matrix:
            for x in row:
                a += ("{:4d}".format(x)) + " "
            b = b + a + "\n"
            a = ""
        return b

    def __add__(self, other):
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


matrix_1 = Matrix([[1, 1, 4], [2, 2, 8], [3, 3, 7]])
matrix_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(matrix_1)
print(matrix_1 + matrix_2)
