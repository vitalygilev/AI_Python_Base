def check_matrix(matrix):
    if not matrix:
        raise Exception("Matrix is empty!")
    if not matrix[0]:
        raise Exception("Matrix is empty!")
    if sum(map(len, matrix)) / len(matrix) != len(matrix[0]):
        raise Exception("Argument isn't a matrix!")


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = []
        check_matrix(self.matrix)
        check_matrix(other.matrix)
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise Exception('Dimensions mismatch!')
        for i in range(len(self.matrix)):
            result.append([x + y for x, y in zip(self.matrix[i], other.matrix[i])])
        return result

    def __str__(self):
        return '\n'.join(map(lambda row: ' '.join(map(str, row)), self.matrix))


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
try:
    print('Matrix 1:', matrix1, sep="\n")
    print('Matrix 2:', matrix2, sep="\n")
    print('Sum = \n', Matrix(matrix1 + matrix2))
except Exception as e:
    print("Error ", e)
