class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        curMax = 0
        for x in nums:
            temp = curMax
            curMax = max(prevMax + x, curMax)
            prevMax = temp
        return curMax




class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        re = []
        re.append(0)
        re.append(nums[0])
        for i in range(1, len(nums)):
            re.append(max(re[i-1] + nums[i], re[i]))
        return re[-1]
            