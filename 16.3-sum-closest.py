#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

class Solution:
    def threeSumClosest(self, nums, target) -> int:
        # Sorted Array
        nums.sort()
        print(nums)
        arr_size = len(nums)
        diff = float("inf")
        # re = []
        for i in range(0, arr_size-2):
            l = i + 1
            r = arr_size - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r] - target
                if abs(temp) < diff:
                    diff = abs(temp)
                    summ = temp + target
                if temp > 0:
                    r -= 1
                else: 
                    l += 1
        return summ

# a = Solution()
# nums = [-1,2,1,-4]
# target = 1
# print(a.threeSumClosest(nums, target))
