class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        n = len(nums)            
        while p2 < n:
            if nums[p1] == 0 and nums[p2]!=0:
                self.swap(nums, p1, p2)            
            if nums[p1]!=0:
                p1+=1
            p2+=1
    
    def swap(self, nums, p1, p2):
        temp = nums[p1] 
        nums[p1] = nums[p2]
        nums[p2] = temp
        