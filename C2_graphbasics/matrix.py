class Matrix:
    """
    mat_content should be a list with m sub lists, each containing n elements
    where the dimension should be a tuple (m, n)

    mat_type specification:
    default is "any", where you can type in your own values
    "id" stands for identity, which generates identity matrix with dimension of your choice
    "zero" generates zero matrix with dimension of your choice
        in both situations the mat_content does not matter, but should be set as an empty list
    """
    def __init__(self, mat_content, dimension, mat_type="any"):
        self.mat_content = mat_content
        self.dimension = dimension
        self.mat_type = mat_type

        if self.mat_type == "zero":
            self.mat_content = []
            row = []
            for i in range(self.dimension[1]):
                row.append(0)
            for j in range(self.dimension[0]):
                self.mat_content.append(row.copy())
                # if it's only "append(row)" all subsequent calculations will treat them as the same thing

        elif self.mat_type == "id":
            if self.dimension[0] != self.dimension[1]:
                raise AttributeError("Matrix in this dimension doesn't have identity matrix")
            else:
                self.mat_content = []
                row = []
                for i in range(self.dimension[1]):
                    row.append(0)
                for j in range(self.dimension[0]):
                    self.mat_content.append(row.copy())
                    self.mat_content[-1][j] = 1

        else:
            if type(self.mat_content) is not list:
                raise TypeError
            if type(self.dimension) is not tuple:
                raise TypeError
            if len(self.mat_content) != self.dimension[0]:
                raise IndexError("Dimension Error: incorrect number of rows")
            for row in self.mat_content:
                if len(row) != self.dimension[1]:
                    raise IndexError("Dimension Error: incorrect number of columns")

    def copy(self):
        return Matrix(self.mat_content, self.dimension, self.mat_type)

    # states dimension and writes out all elements
    def __str__(self):
        return f"matrix with dimension {self.dimension}:\n" + "\n".join(str(row) for row in self.mat_content)

    # same dimension and elements are all identical
    def __eq__(self, other):
        if other.dimension != self.dimension:
            return False
        else:
            for i in range(other.dimension[0]):
                for j in range(other.dimension[1]):
                    if other.mat_content[i][j] != self.mat_content[i][j]:
                        return False
        return True

    # only matrices with the same dimension
    def __add__(self, other):
        if other.dimension != self.dimension:
            raise AttributeError("Cannot add matrices with different dimensions")
        else:
            result = self.copy()
            for i in range(result.dimension[0]):
                for j in range(result.dimension[1]):
                    result.mat_content[i][j] += other.mat_content[i][j]
        return result

    # only matrices with the same dimension
    def __sub__(self, other):
        if other.dimension != self.dimension:
            raise AttributeError("Cannot add matrices with different dimensions")
        else:
            result = self.copy()
            for i in range(result.dimension[0]):
                for j in range(result.dimension[1]):
                    result.mat_content[i][j] -= other.mat_content[i][j]
        return result

    # scalar factor AND by matrix
    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            result = self.copy()
            for i in range(result.dimension[0]):
                for j in range(result.dimension[1]):
                    result.mat_content[i][j] *= other
            return result
        elif type(other) is Matrix:
            if other.dimension[0] != self.dimension[1]:
                raise AttributeError("Two matrices can only be multiplied together if the number of columns of one equals to the number of rows of the other one")
            else:
                com_num = self.dimension[1]     # number of multiplication for each element in result
                result = Matrix([], (self.dimension[0], other.dimension[1]), "zero")
                for i in range(result.dimension[0]):
                    for j in range(result.dimension[1]):
                        for k in range(com_num):
                            result.mat_content[i][j] += self.mat_content[i][k] * other.mat_content[k][j]
                return result

    # determinant of 2x2 and 3x3 matrices
    def det(self):
        if self.dimension[0] != self.dimension[1]:
            raise AttributeError("Non-square matrices do not have determinant")
        elif self.dimension[0] >= 4:
            raise OverflowError("This humble lil programme cannot handle 5x5 or larger matrices yet")
        else:
            if self.dimension[0] == 2:
                return self.mat_content[0][0] * self.mat_content[1][1] - self.mat_content[0][1] * self.mat_content[1][0]
            elif self.dimension[0] == 3:
                determinant = 0
                for i, coe in enumerate(self.mat_content[0]):
                    line_1 = self.mat_content[1].copy()
                    del line_1[i]
                    line_2 = self.mat_content[2].copy()
                    del line_2[i]
                    determinant += (-1 if i == 1 else 1) * coe * (line_1[0] * line_2[1] - line_1[1] * line_2[0])
                return determinant

    def inverse(self, keep=False):
        det = self.det()
        if det == 0:
            raise AttributeError("This matrix is singular, it does not have an inverse")
        else:
            if self.dimension[0] == 2:
                inverse = self.copy()
                inverse.mat_content[0][1] *= -1
                inverse.mat_content[1][0] *= -1
                if keep:
                    print(f"the inverse of'\n{self}' is:\n1 / {det} times\n{inverse}")
                return inverse * (1 / det)
            elif self.dimension[0] == 3:
                pass


print(Matrix([[2, 3, 5], [-4, 1, 0], [-2, -1, 7]], (3, 3)).det())
