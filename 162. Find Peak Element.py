# O(n) solution, check all elements
class Solution:
    def isPeak(self, arr, n):
        if n==0:
            if arr[n] > arr[n+1]:
                return True
            else:
                return False
        if n == len(arr)-1:
            if arr[n] > arr[n-1]:
                return True
            else:
                return False
        elif arr[n] > arr[n-1] and arr[n] > arr[n+1]:
            return True
        return False
            
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return nums.index(max(nums))
        for i in range(len(nums)):
            if self.isPeak(nums, i):
                return i

    # Binary Search Solution  
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums=len(nums)
        if len_nums == 0: return -1
        if len_nums == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[len_nums-1] > nums[len_nums-2]: return len_nums-1
        
        left=1
        right=len_nums-2
        
        while right >= left:
            mid=left+(right-left)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: 
                return mid
            elif nums[mid] > nums[mid-1]: 
                left=mid+1
            else: 
                right=mid-1  
