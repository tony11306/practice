def transpose(matrix):
    newMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            newMatrix[i][j] = matrix[j][i]

    return newMatrix

def printMatrix(matrix):
    print("---------")
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print("")
    print("---------")

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


# main
if __name__ == '__main__':

    fromBasis = []
    transitionMatrix = []
    inpt = list(map(float, input().split())) # the fromBasis input
    print(inpt)
    k = 0
    for i in range(int(len(inpt)**0.5)):
        fromBasis.append([])
        for j in range(int(len(inpt)**0.5)):
            fromBasis[i].append(inpt[k])
            k += 1

    # fromBasis = transpose(fromBasis)

    inpt = list(map(float, input().split())) # the toBasis input
    toBasis = []
    k = 0
    for i in range(int(len(inpt)**0.5)):
        toBasis.append([])
        for j in range(int(len(inpt)**0.5)):
            toBasis[i].append(inpt[k])
            k += 1
    # toBasis = transpose(toBasis)

    # combind fromBasis and toBasis together

    for i in range(len(fromBasis)):
        for j in range(len(fromBasis[i])):
            toBasis[i].append(fromBasis[i][j])

    matrix = gaussElimination(toBasis, len(toBasis))
    for i in range(len(matrix)):
        transitionMatrix.append([])
        for j in range(len(matrix), len(matrix[i])):
            transitionMatrix[i].append(matrix[i][j])


    inpt = list(map(float, input().split()))
    coordinate = []
    for i in range(len(inpt)):
        coordinate.append([])
        coordinate[i].append(inpt[i])
    
    ans = multiply(transitionMatrix, coordinate)
    print(matrix)
    print(transitionMatrix)
    print(ans)
