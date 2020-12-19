class Solution:
    """
    @param n: the number of people
    @param m: the number of groups
    @return: the number of grouping options
    """
    def groupingOptions(self, n, m):
        # write your code here
        # memoization
        if n < m:
            return 0

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, m+1):
            dp[i][i] = 1
            
        for i in range(2, n+1):
            for j in range(1, min(i,m)+1):
                for k in range(1, min(j+1, i-j+1)):
                    dp[i][j] += dp[i - j][k]
        
        return dp[n][m]

    #   for (int i = 2; i <= n; ++i) {
    #         for (int j = 1; j <= min(i, m); ++j) { 
    #             for (int k = 1; k <= j; ++k) {
    #                 dp[i][j] += dp[i - j][k];       