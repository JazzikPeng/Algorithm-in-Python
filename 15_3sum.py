class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        re = []
        if len(nums) == 3 and sum(nums) == 0:
            re.append(nums)
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] > nums[i-1]:
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    summ = nums[i] + nums[start] + nums[end]
                    # print(summ)
                    if summ == 0:
                        re.append([nums[i], nums[start], nums[end]])
                    if summ < 0:
                        curr_start = start
                        while nums[start] == nums[curr_start] and start < end:
                            start += 1
                    else:
                        curr_end = end
                        while nums[end] == nums[curr_end] and start < end:
                            end -= 1
        return re
