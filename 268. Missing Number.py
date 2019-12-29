class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=  set(list(range(len(nums)+1))) - set(nums)
        return t.pop()


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return (len(nums) * (len(nums) + 1) / 2) - sum(nums)


# Solve with bitwise operation

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit operation
        re = len(nums)
        for idx, i in enumerate(nums):
            re = idx ^ i ^ re
            
        return re

