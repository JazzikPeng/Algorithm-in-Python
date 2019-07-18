# Use Greedy Search
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        reach, i = 0, 0
        for i in range(len(nums)):
            if i > reach:
                break
            reach = max(nums[i]+i, reach)
            if reach >= len(nums) -1:
                return True
        return False




s = Solution()
print(s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
