class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:                           
                nums[abs(nums[i])-1]*=-1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        


# Set solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return None
        n = len(nums)
        t = set(nums)
        return list(set(list(range(1,n+1))) - t)