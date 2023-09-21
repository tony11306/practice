import math

def my_matrix_chain(p, n):
    '''
    p: n個矩陣的row和column
    n: 代表有多少個矩陣
    '''
    dp = [[math.inf for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0
        if i < n-1:
            dp[i][i+1] = p[i] * p[i+1] * p[i+2]
    
    # m 個矩陣相乘
    for m in range(2, n + 1):
        # 第 i 個矩陣開始, 0 based
        for i in range(n - m + 1):
            for j in range(i + 1, i + m):
                dp[i][i+m-1] = min(dp[i][i+m-1], dp[i][j-1] + dp[j][i+m-1] + p[i] * p[j] * p[i+m])
                
    return dp[0][n-1]
        
 
# Driver program to test above function
arr = [30, 35, 15, 5, 10, 20, 25, 58, 14, 35, 68, 11]
size = len(arr)

print("Minimum number of multiplications is " +
       str(my_matrix_chain(arr, size-1)))
