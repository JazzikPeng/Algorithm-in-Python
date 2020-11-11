class Solution:
    def numTilings(self, N):
        mod = 10**9 + 7
        dp = [[0 for x in range(2)] for y in range(N+1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][1]
            dp[i][1] = dp[i-2][0] + dp[i-1][1]

        return dp[N][0] % mod
    

"""
dp[N][2]

dp[N][0]


X
X

1. 
X
X

2.
-
X



YY
X

XY
XY

XX
YY

XY
YY

YY
XY

"""
