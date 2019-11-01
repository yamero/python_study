import math
from matplotlib import pyplot as plt
from playLA.Matrix import Matrix

if __name__ == '__main__':
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4], [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x_list = [point[0] for point in points]
    y_list = [point[1] for point in points]

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.plot(x_list, y_list)
    #plt.show()

    ''' 矩阵变换应用 '''
    P = Matrix(points).T()
    #T = Matrix([[1.5, 0], [0, 1.5]]) #x，y方向都放大1.5倍
    #T = Matrix([[0.5, 0], [0, 0.5]]) #x,y方向都缩小0.5倍
    #T = Matrix([[1, 0], [0, -1]]) #垂直翻转
    #T = Matrix([[-1, 0], [0, 1]]) #水平翻转
    #T = Matrix([[-1, 0], [0, -1]])  #原点翻转
    #T = Matrix([[1, 0.3], [0, 1]])  #x正方向错切
    #T = Matrix([[1, -0.3], [0, 1]])  # x负方向错切
    #T = Matrix([[1, 0], [0.5, 1]])  # y正方向错切
    #T = Matrix([[1, 0], [-0.5, 1]])  # y正方向错切

    angle = math.pi / 3
    T = Matrix([[math.cos(angle), math.sin(angle)], [-math.sin(angle), math.cos(angle)]]) #顺时针旋转60度

    Q = T.dot_mat(P)
    x_list = [Q.col_vec(i)[0] for i in range(Q.col_num())]
    y_list = [Q.col_vec(i)[1] for i in range(Q.col_num())]

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x_list, y_list)
    plt.show()