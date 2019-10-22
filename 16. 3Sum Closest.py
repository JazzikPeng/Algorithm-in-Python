class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l  < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(val - target) < abs(result - target):
                    result = val
                if val == target:
                    return target
                elif val < target:
                    l += 1
                elif val > target:
                    r -= 1
        return result
                