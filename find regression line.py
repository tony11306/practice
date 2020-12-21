def transpose(matrix):
    newMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            newMatrix[i][j] = matrix[j][i]

    return newMatrix

def gaussElimination(matrix, n: int):

    def swapRow(a, b):
        matrix[a], matrix[b] = matrix[b], matrix[a]
    
    def removeNegativeZero():
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if abs(matrix[i][j]) < 0.000000001:
                    matrix[i][j] = 0.0
    
    for i in range(n): # 控制橫向
        maxIndex = i
        for j in range(i, n): # 控制縱向
            if abs(matrix[maxIndex][i]) < abs(matrix[j][i]):
                maxIndex = j
        swapRow(maxIndex, i)
        # printMatrix(matrix)
        val = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] /= val
        for j in range(i+1, n):
            val = matrix[j][i]
            for k in range(i, len(matrix[j])):
                matrix[j][k] += matrix[i][k]*(-val)
                

    for i in range(n-2, -1, -1): # 1 0
        for j in range(i, -1, -1): # 1 0
            val = matrix[j][i+1]
            for k in range(i, len(matrix[i])):
                matrix[j][k] += matrix[i+1][k]*(-val)
                
    removeNegativeZero()
    return matrix

def multiply(matrixA, matrixB):
    result = []
    for i in range(len(matrixA)):
        result.append([])
        for j in range(len(matrixB[i])):
            val = 0
            for k in range(len(matrixA[i])):
                val += matrixA[i][k] * matrixB[k][j]
            result[i].append(val)

    return result

def getIdentityMatrix(n: int):
    matrix = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        matrix[i][i] = 1

    return matrix


def getInverse(matrix):
    identityMatrix = getIdentityMatrix(len(matrix))
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i].append(identityMatrix[i][j])
    
    matrix = gaussElimination(matrix, n)
    result = []

    for i in range(n):
        result.append([])
        for j in range(n, 2*n):
            result[i].append(matrix[i][j])
    return result

# main
if __name__ == '__main__':
    tests = int(input())
    n = int(input())
    positions = []
    for i in range(tests):
        positions.append(list(map(float, input().split())))
    matrix = []
    yMatrix = []
    for i in range(len(positions)):
        matrix.append([])
        yMatrix.append([positions[i][1]])
        for j in range(n+1):
            matrix[i].append(pow(positions[i][0], j))
    transposeMatrix = transpose(matrix)
    result = multiply(getInverse(multiply(transposeMatrix, matrix)), multiply(transposeMatrix, yMatrix))
    print(result)

    for i in result:
        if abs(i) < 0.000000001:
            print(f'0.00', end=' ')
        else:
            print(f'{i[0]:.2f}', end=' ')
