def getDetValue(matrix, det_size):
    '''
    @param matrix: The square matrix you want to get the det(matrix) value.
    Make sure that the matrix is a square matrix. Otherwise, it might have some errors if you call it.

    -How does the cofactor work writing in code?
    It is based on recursion.

    For example, say we have a matrix:
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    The matrix_size is 3('cause it's a 3*3 matrix). 
    By using the cofactor method, the determinant of the matrix works like this:

    1*|5 6| + (-1)*2*|4 6| + 3*|4 5|
      |8 9|          |7 9|     |7 8|

    Noticed something? we have to get the determinants of the 3 cofactors, and then we are able to return the value.
    The 3 cofactors are also square matrices, and that means we can call getDetValue(matrix) again.
    Let's make it more like code.
    -----------------------------------------
        cofactor1 = [[5, 6], [8, 9]]
        cofactor2 = [[4, 6], [7, 9]]
        cofactor3 = [[4, 5], [7, 8]]

        det1 = getDetValue(cofactor1)
        det2 = getDetValue(cofactor2)
        det3 = getDetValue(cofactor3)

        value = 1*det1 + (-1)*2*det2 + 3*det3
    -----------------------------------------
    Now let's get into getDetValue(cofactor1) and see how it works.
    So the matrix in this function is now [5, 6].
                                          [8, 9]
    The cofactors are [9] and [8], and they are also square matrices, which means we can call getDetValue(matrix) again.
    -----------------------------------------
    Let's step into getDetValue([[8]])
    The matrix in this function is [[8]], which is a 1*1 matrix. 
    At this point we want to stop since it's simply just a single value.
    So what we will do is to return matrix[0][0]. (Remember, a matrix is always a 2d list)
    -----------------------------------------
    Now we know the determinant of [[8]] and [[9]], which means we know the determinant of [[5, 6], [8, 9]], 
    which also means we know the determinant of [[1, 2, 3],[4, 5, 6],[7, 8, 9]], because the others is also work the same way
    
    And that is basically the concept of my function.
    '''
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
li = input().split()
k = 0
for i in range(det_size):
	for j in range(det_size):
		matrix[i].append(int(li[k]))
		k += 1
print(getDetValue(matrix, det_size))
