class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        n = len(A)
        if n < 2:
            return 0
        
        range_sum = self.get_range_sum(A)
        
        dp = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  
                for mid in range(i, j):
                    # dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + sum(A[i:j+1]))
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + range_sum[i][j])
        return dp[0][n - 1]
                
        
        
    def get_range_sum(self, A):
        n = len(A)
        
        range_sum = [[0] * n for _ in range(len(A))]
        
        for i in range(n):
            range_sum[i][i] = A[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j-1] + A[j]
        
        return range_sum