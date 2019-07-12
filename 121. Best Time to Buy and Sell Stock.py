# Convert This problem to a max subarray problem
# Problem 53.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Compute difference then find the max sub array
        if len(prices) < 2:
            return 0
        arr = [x-y for x, y in zip(prices[1:], prices[:-1])]
        max_num = 0
        max_now = 0
        if max(arr) < 0:
            return 0
        for i in arr:
            max_now += i
            if max_now < 0:
                max_now = 0
            if max_now > max_num:
                max_num = max_now
        return max_num

# Solve with one pass by dynamically keep the
# min stock price


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Compute difference then find the max sub array
        min_p = float("inf")
        max_profit = 0
        for i in prices:
            if i < min_p:
                min_p = i
            if i - min_p > max_profit:
                max_profit = i - min_p
        return max_profit
