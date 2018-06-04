class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) <2:
            return 0
        res = 0
        curMaxArea =0
        maxNext = 0
        for i in range(len(nums)- 1):
            maxNext = max(maxNext, i+nums[i])
            if i == curMaxArea:
                res+=1
                curMaxArea = maxNext
        return res

    def jump2(nums):
        if nums == None or len(nums) <2:
            return 0
        res = 0
        curMaxArea =0
        maxNext = 0
        for i in range(len(nums)- 1):
            maxNext = max(maxNext, i+nums[i])
            if i == curMaxArea:
                res+=1
                curMaxArea = maxNext
        return res