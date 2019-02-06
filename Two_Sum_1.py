class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # fill initial set/dict
        s = {target-nums[0]}
        d = {nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in s:
                return [d[target-nums[i]], i]
            else:
                s.add(target-nums[i])
                d[nums[i]] = i
        return None
