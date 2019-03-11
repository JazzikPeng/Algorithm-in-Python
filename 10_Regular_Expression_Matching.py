class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for col in range(len(p)+1)] for row in range(len(s)+1)]
        if s is None or p is None:
            return False
        if p == '*':
            return True
        if s == p:
            return True
        dp[0][0] = True
        # 预处理
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i-1]:
                dp[0][i+1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                # condition 1
                # print(i, j )
                if p[j] == s[i]:
                    dp[i+1][j + 1] = dp[i][j]
                if p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = (dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1])
        return dp[len(s)][len(p)] == 1
