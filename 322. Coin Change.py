class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [n] * n
        dp[0] = 0 
        for i in range(1, n):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        if dp[amount] > amount:
            return -1
        return dp[amount]
        