class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10**9 + 7 
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(1, len(s)):
            if s[i] == '*':
                dp[i+1] = 9 * dp[i]
                if s[i-1] == '1':
                    dp[i+1] = dp[i+1] + 9 * dp[i-1]
                elif s[i-1]=='2':
                    dp[i+1] = dp[i+1] + 6 * dp[i-1]
                elif s[i-1] == '*':
                    dp[i+1] = dp[i+1] + 15 * dp[i-1]
            else:
                dp[i+1] = dp[i] if s[i]!='0' else 0
                if s[i-1] == '1':
                    dp[i+1] = dp[i+1] + dp[i-1]
                elif s[i-1] == '2' and s[i] <= '6':
                    dp[i+1] = dp[i+1] + dp[i-1]
                elif s[i-1] == '*':
                    dp[i+1] = dp[i+1] + (2 if s[i] <='6' else 1) * dp[i-1]
        # print(dp)
        return int(dp[len(s)]) % mod



class Solution(object):
    def numDecodings(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c < = '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0