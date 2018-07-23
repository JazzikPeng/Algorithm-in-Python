class Solution:
    # Solution 1, similar to find the pivot solution
    def find_pivot(self, nums):
        if len(nums) <= 2:
            return nums.index(min(nums))
        left, right = 0, len(nums) - 1
        while right > left:
            if right - left == 1:
                return nums.index(min(nums[left:right+1]))
            mid = (left + right) // 2 
            if nums[mid] < nums[right]: # Pivot is in mid to right
                right = mid 
            else:
                left = mid
           # print(nums[left], nums[right], left, right)
        return -1     
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = self.find_pivot(nums)
        return nums[idx]

    # Solution 2
    def findMin2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lo, hi = 0, len(nums)-1
    while lo < hi - 1:
        m = (lo+hi)//2
        if nums[m] <= nums[hi]:
            hi = m
        elif nums[lo] <= nums[m]:
            lo = m

    return min(nums[lo], nums[hi])