def matrix_struct(matrix, index):
    lint = []
    lout = []
    for i in range(1,len(matrix)):
        for j in range(len(matrix)):
            if j==index: pass
            else: lint.append(matrix[i][j])
        lout.append(lint)
        lint = []
    return lout

def determinant(matrix):
    mlen = len(matrix)
    if mlen==1: return matrix[0][0]
    elif mlen==2: return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    else:
        sum = 0
        for i in range(len(matrix)):
            if i%2 != 0: sum += -1 * matrix[0][i] * determinant(matrix_struct(matrix, i))
            else: sum += 1 * matrix[0][i] * determinant(matrix_struct(matrix, i))

        return sum

m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]

assert determinant([[1]]) == 1
assert determinant(m1) == -1
assert determinant(m2) == -20

