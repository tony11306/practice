def getDetValue(matrix, det_size):
	if det_size == 1:
		return matrix[0][0]
	cofactor = [[0 for __ in range(det_size-1)] for _ in range(det_size-1)]
	value = 0
	for i in range(det_size):
		for j in range(1, det_size):
			a = 0
			for k in range(det_size):
				if k != i:
					cofactor[j-1][a] = matrix[j][k]
					a += 1
		if(i % 2 == 1):
			value += -1 * matrix[0][i] * getDetValue(cofactor, det_size-1)
		else:
			value += 1 * matrix[0][i] * getDetValue(cofactor, det_size -1)
	return value

det_size = int(input())
matrix = [[] for _ in range(det_size)]
inverse = [[0 for __ in range(det_size)] for _ in range(det_size)]
cofactor = [[0 for __ in range(det_size-1)] for _ in range(det_size-1)]
li = input().split()
k = 0
for i in range(det_size):
	for j in range(det_size):
		matrix[i].append(int(li[k]))
		k += 1

detValue = getDetValue(matrix, det_size)
if detValue != 0:
    for i in range(det_size):
        for j in range(det_size):
            row = 0
            col = 0
            for k in range(det_size):
                if k == j:
                    continue
                for l in range(det_size):
                    if l != i:
                        cofactor[row][col] = matrix[k][l]
                        col += 1
                col = 0
                row += 1
            if (i+j) % 2 == 0:
                inverse[i][j] = getDetValue(cofactor, det_size-1) / detValue
            else:
                inverse[i][j] = -1 * getDetValue(cofactor, det_size-1) / detValue
                
    print(inverse)
else:
    print('The matrix is singular')
