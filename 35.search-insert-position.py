#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        for i in nums:
            if i==target:
                return idx
            if i>target:
                return idx
            idx += 1
        return idx
