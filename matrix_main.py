from  playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    m1 = Matrix([[1, 2], [3, 4]])
    #print(m1)
    #print(m1.row_num())
    #print(len(m1))
    #print(m1.col_num())
    #print(m1.shap())
    #print(m1.size())
    #print(m1[1, 2])
    #print(m1.row_vec(1))
    #print(m1.col_vec(2))
    m2 = Matrix([[0, 4, 5], [0, 0, 3]])
    #print(m1 + m2)
    #print(m1 - m2)
    #print(m2 * 2)
    #print(2 * m2)
    #print(m2 / 2)
    #print(+m2)
    #print(-m2)
    #print(m1.dot_mat(m2))
    print(m1.T())

    v1 = Vector([3, 2])
    #print(v1)
    #print(m1.dot_vec(v1))

    z = Matrix.zero(3, 2)
    #print(z)