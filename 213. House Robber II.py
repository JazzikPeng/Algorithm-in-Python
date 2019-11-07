class Solution:
    def helper(self, nums: List[int]) -> int:
        prevMax = 0
        curMax = 0
        for x in nums:
            temp = curMax
            curMax = max(prevMax + x, curMax)
            prevMax = temp
        return curMax
    
    
    def rob(self, nums: List[int]) -> int:
        c = nums[0] if nums else 0
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), c)