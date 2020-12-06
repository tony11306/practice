# 此程式沒有對無解和無限多組解作處理
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
            if abs(matrix[maxIndex][i]) < abs(matrix[j][i]): # 找出絕對值最大值，移到上層，用意是為了不要出現領導係數為0的狀況
                maxIndex = j
        swapRow(maxIndex, i)
        val = matrix[i][i]
        for j in range(len(matrix[i])): # 把領導係數變成1
            matrix[i][j] /= val
        for j in range(i+1, n): # 開始對下面列做消去
            val = matrix[j][i]
            for k in range(i, len(matrix[j])):
                matrix[j][k] += matrix[i][k]*(-val)
                

    for i in range(n-2, -1, -1): # 處理上三角
        for j in range(i, -1, -1):
            val = matrix[j][i+1]
            for k in range(i, len(matrix[i])): # 往上做消去
                matrix[j][k] += matrix[i+1][k]*(-val)
                
    removeNegativeZero()
    return matrix
