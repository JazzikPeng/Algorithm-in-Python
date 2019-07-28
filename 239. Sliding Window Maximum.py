class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Build a array of length K
        re = []
        sw = [None for x in range(k)]
        for i in range(k, len(nums)+1):
            m = max(nums[i-k:i])
            re.append(m)
        return re

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return None
        # Build a array of length K
        re = []
        sw = [None for x in range(k)]
        sw = nums[:k]
        for i in range(k, len(nums)+1):
            m = max(sw)
            sw.pop(0)
            try:
                sw.append(nums[i])
            except:
                pass
            re.append(m)
        return re