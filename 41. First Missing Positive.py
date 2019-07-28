class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
            
        t = set(list(range(1, len(nums)+1))) - set(nums)
        if len(t)==0:
            return max(nums) + 1
        while len(t) > 0:
            t_m = min(t)
            if t_m <= 0:
                t.discard(t_m)
            else:
                return t_m


# This problem require constant space,
# We need to consider using both index and value to support constant space 
# Operation
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        # Modify the nums array so that all the positive
        # number is in front, first j numbers are positive
        j = 0 
        for i in nums:
            if i > 0:
                nums[j] = i
                j += 1

        for i in range(j): # Traverse all the positive numbers
            if abs(nums[i]) <= j and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] *= -1

        for i in range(j):
            if nums[i] > 0:
                return i + 1

        return j + 1

