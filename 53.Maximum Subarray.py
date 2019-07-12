class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(1)
        if max(nums) < 0:
            return max(nums)
        max_num = 0
        counter = 0
        n = len(nums)
        for i in range(n):
            counter += nums[i]
            if counter < 0:
                counter = 0
            if counter > max_num:
                max_num = counter
        return max_num
