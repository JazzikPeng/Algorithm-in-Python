# You can use double pointer similar to quick sort

class Solution:
    def sortColors(self, nums):
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # O(n)
        # Bucket sort
        a,b,c=0,0,0
        for i in nums:
            if i == 0:
                a+=1
            elif i==1:
                b+=1
            elif i == 2:
                c+=1
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
                
            if i < a+b and i >= a:
                nums[i] = 1
                
            if i >= a+b:
                nums[i] = 2

        