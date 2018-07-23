class Solution:
    def normal_search(self, nums, target):
        left, right = 0, len(nums)-1
        while right >= left:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return -1 
    
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
            print(nums[left], nums[right], left, right)
        return -1     
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        # Use O(log n) to find the Pivot
        left, right = 0, len(nums) - 1
        # This is a un-rotated array, since no duplication
        print(right, left)
        if nums[right] > nums[left]:
            return self.normal_search( nums, target)
        else: # This when the array is roated, we need to find the idx of pivot
            pivot = self.find_pivot(nums)
            print('pivot', pivot)
            if nums[pivot] == target:
                print('pivot', pivot)
                return pivot
            else:
                nums = nums[pivot:] + nums[:pivot]
                idx = self.normal_search(nums, target)
                print('idx', idx)
                if idx==-1:
                    return -1
                else:
                    return (pivot+idx) % len(nums)
                    
            