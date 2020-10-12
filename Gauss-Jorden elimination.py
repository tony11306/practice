def solve(matrix):

    ans = []
    n = len(matrix)
    # ------------------------------------------------------
    '''
    This part will eliminate lower triangular
    '''
    for i in range(n):
        if matrix[i][i] == 0:
            for rowIndex in range(i+1, len(matrix)):
                if matrix[rowIndex][i] != 0:
                    matrix = rowSwap(matrix, i, rowIndex)
                    break

        for j in range(i, n):
          
            if matrix[j][i] == 0:
                continue
            lcmNum = lcm(matrix[i][i], matrix[j][i])
            matrix = rowMultiply(matrix, j, lcmNum // matrix[j][i])
            matrix = rowMultiply(matrix, i, -lcmNum // matrix[i][i])
            matrix = rowAdd(matrix, j, i)
    # ------------------------------------------------------  
    if matrix[n-1][n] == 0 and matrix[n-1][n-1] == 0: # if last row become 0 0 0 .... 0 0, then it has infinite solutions.
        printMatrix(matrix)
        print('無限多組解')
        return
    elif matrix[n-1][n] != 0 and matrix[n-1][n-1] == 0: # if last row become 0 0 0 ... 0 k, where k != 0, then it has no solution.
        printMatrix(matrix)
        print('無解')
        return
    # -------------------------------------------------------
    '''
    This part will eliminate the upper triangular
    '''
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if matrix[j][i] == 0:
                continue
            lcmNum = lcm(matrix[i][i], matrix[j][i])
            matrix = rowMultiply(matrix, j, lcmNum // matrix[j][i])
            matrix = rowMultiply(matrix, i, -lcmNum // matrix[i][i])
            matrix = rowAdd(matrix, j, i)
    printMatrix(matrix)
    for i in range(n):
        ans.append(matrix[i][n] / matrix[i][i])
    return ans
        
def lcm(a: int, b: int):
    '''
    This function returns the least common multiple
    '''
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)

def gcd(a: int, b: int):
    '''
    This function returns the greatest common divisor of a and b
    '''
    if a == 0 or b == 0:
        return 0

    if a > b: # make sure that a is smaller than b, since we're gonna do swap first and then divide in the while loop
        temp = a
        a = b
        b = temp
    while a != 0:
        # swap a and b
        temp = a
        a = b
        b = temp

        a %= b
        
    return b

def printMatrix(matrix):
    print('')
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print('')

def rowMultiply(matrix, rowIndex, k):
    '''
    This function will return the matrix where its rowIndex'th row is multipied by k.
    '''
    for i in range(len(matrix[rowIndex])):
        matrix[rowIndex][i] *= k

    return matrix

def rowAdd(matrix, firstRowIndex, secondRowIndex):
    '''
    This function will add the second row to the first row, and then return the matrix.
    '''
    for i in range(len(matrix[firstRowIndex])):
        matrix[firstRowIndex][i] += matrix[secondRowIndex][i]
    
    return matrix

def rowSwap(matrix, firstRowIndex, secondRowIndex):
    '''
    This function will swap matrix[firstRowIndex] and matrix[secondRowIndex].
    '''
    for i in range(len(matrix[firstRowIndex])):
        temp = matrix[firstRowIndex][i]
        matrix[firstRowIndex][i] = matrix[secondRowIndex][i]
        matrix[secondRowIndex][i] = temp
    return matrix



print(f'n元一次聯立方程式?')
n = int(input())
print(f'請每列輸入{n+1}個元素，共{n}列')

matrix = []
for i in range(n):
    matrix.append([])
    rows = input().split()
    for row in rows:
        matrix[i].append(int(row))

ans = solve(matrix)
print(ans)
        

