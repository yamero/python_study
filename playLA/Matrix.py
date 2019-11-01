from .Vector import Vector

class Matrix(object):

    def __init__(self, lst2d):
        self._values = [row[:] for row in lst2d]

    def __iter__(self):
        return self._values.__iter__()

    @classmethod
    def zero(self, r, c):
        ''' 获取一个r行c列的零矩阵 '''
        return Matrix([[0] * c for _ in range(r)])

    def T(self):
        ''' 矩阵转置（行变列，列变行） '''
        return Matrix([[v for v in self.col_vec(i)] for i in range(self.col_num())])

    def dot_vec(self, other):
        ''' 矩阵与向量相乘 '''
        if self.col_num() != len(other):
            print('矩阵的列数必须与向量的维度相同')
            return False
        return Vector([other.dot(self.row_vec(i)) for i in range(self.row_num())])

    def dot_mat(self, other):
        ''' 矩阵与矩阵相乘 '''
        if self.col_num() != other.row_num():
            print('第一个矩阵的列数必须与第二个矩阵的行数相同')
            return False
        return Matrix([[self.row_vec(i).dot(other.col_vec(j)) for j in range(other.col_num())] for i in range(self.row_num())])

    def __add__(self, other):
        ''' 两个矩阵相加 '''
        if self.shap() != other.shap():
            print('两个矩阵大小必须相同')
            return False
        return Matrix([[a + b for a, b in zip(self.row_vec(i), other.row_vec(i))] for i in range(self.row_num())])

    def __sub__(self, other):
        ''' 两个矩阵相减 '''
        if self.shap() != other.shap():
            print('两个矩阵大小必须相同')
            return False
        return Matrix([[a - b for a, b in zip(self.row_vec(i), other.row_vec(i))] for i in range(self.row_num())])

    def __mul__(self, k):
        ''' 矩阵数乘（矩阵在数的左边） '''
        return Matrix([[k * v for v in self.row_vec(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        ''' 矩阵数乘（矩阵在数的右边） '''
        return Matrix([[k * v for v in self.row_vec(i)] for i in range(self.row_num())])

    def __truediv__(self, k):
        ''' 矩阵数除 '''
        return 1 / k * self

    def __pos__(self):
        ''' 矩阵取正 '''
        return 1 * self

    def __neg__(self):
        ''' 矩阵取负 '''
        return -1 * self

    def row_vec(self, index):
        ''' 获取矩阵第index行向量 '''
        return Vector(self._values[index])

    def col_vec(self, index):
        ''' 获取矩阵第index列向量 '''
        return Vector([row[index] for row in self._values])

    def row_num(self):
        ''' 获取矩阵行数 '''
        return len(self._values)

    __len__ = row_num

    def col_num(self):
        ''' 获取矩阵列数 '''
        return len(self._values[0])

    def shap(self):
        ''' 获取矩阵形状（几行，几列） '''
        return self.row_num(), self.col_num()

    def size(self):
        ''' 获取矩阵大小（行数 x 列数） '''
        r, c = self.shap()
        return r * c

    def __getitem__(self, item):
        ''' 获取矩阵第r行c列的元素 '''
        r, c = item
        return self._values[r][c]

    def __str__(self):
        return 'Matrix(%s)' % self._values