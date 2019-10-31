import math
from ._global import EPSILON

class Vector(object):

    def __init__(self, lst):
        self._values = list(lst) #lst是list类型，传进来肯定是引用，所以将lst复制一份

    def __add__(self, other):
        ''' 两个向量相加 '''
        if len(self) != len(other):
            print('两个向量的维度必须相同！')
            return False
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        ''' 两个向量相减 '''
        if len(self) != len(other):
            print('两个向量的维度必须相同！')
            return False
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        ''' 向量数乘（向量在数的左边） '''
        return Vector([k * v for v in self])

    def __rmul__(self, k):
        ''' 向量数乘（向量在数的右边） '''
        return Vector([k * v for v in self])

    def __truediv__(self, k):
        ''' 向量数除 '''
        return 1 / k * self

    def __pos__(self):
        ''' 向量取正 '''
        return 1 * self

    def __neg__(self):
        ''' 向量取负 '''
        return -1 * self

    def dot(self, other):
        ''' 向量点乘 '''
        if len(self) != len(other):
            print('两个向量的维度必须相同！')
            return False
        return sum([a * b for a, b in zip(self, other)])

    def norm(self):
        ''' 求向量长度（求模） '''
        return math.sqrt(sum([v ** 2 for v in self]))

    def normalize(self):
        ''' 向量规范化（求单位向量） '''
        norm = self.norm()
        if norm <= EPSILON:
            print('向量长度为零，无法规范化')
            return False
        return Vector([v / norm for v in self])

    @classmethod
    def zero(self, dim):
        ''' 返回dim维度的零向量 '''
        return Vector([0] * dim)

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, item):
        return self._values[item]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return 'Vector(%s)' % self._values

    def __str__(self):
        return '(%s)' % ', '.join('%s' % v for v in self._values)
