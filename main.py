import numpy

def del_mat(matrix, row, col):
    k = len(matrix) - 1
    new_matrix = numpy.zeros((k, k))
    p = 0
    for i in range(len(matrix)):
        if i == row:
            continue
        q = 0
        for j in range(len(matrix[i])):
            if j == col:
                continue
            new_matrix[p][q] = matrix[i][j]
            q = q + 1
        p = p + 1
    return new_matrix


def find_mat(matrix, m):
    determinant = 0
    o = 1
    n = m - 1
    if m == 1:
        determinant = matrix[0][0]
        return determinant
    if m == 2:
        determinant = matrix[0][0] * matrix[1][1] - (matrix[1][0] * matrix[0][1])
        return determinant
    if m > 2:
        for i in range(m):
            determinant = determinant + o * matrix[i][0] * find_mat(del_mat(matrix, i, 0), n)
            o = - o
    return determinant


matr = []
with open("input3.txt") as f:
    for line in f:
        matr.append([float(x) for x in line.split()])

m = find_mat(matr, len(matr))
f = open('output.txt', 'a')
f.write(str(int(m))+' ')
f.close

matr = []
with open("input10.txt") as f:
    for line in f:
        matr.append([float(x) for x in line.split()])

m = find_mat(matr, len(matr))
f = open('output1.txt', 'a')
f.write(str(int(m))+' ')
f.close




