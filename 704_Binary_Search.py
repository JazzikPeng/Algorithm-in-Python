class Solution:        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        if(len(nums) <= 0):
            return -1
        
        while(left <= right):
            mid = (left + right) // 2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    def search2(self, nums, target):
        try:
            temp = nums.index(target)
            return temp
        except:
            return -1

    # Binary Search Template #2:
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if left != len(nums) and nums[left] == target:
            return left
        return -1

    # Template #3:
    def binarySearch3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1

import numpy as np 
if __name__ =='__main__':

    temp = np.random.randint(0, 100000, 100000)

    a = [1,2,3,4,5,6]
    b = len(a) -1 
    print((0+b) // 2)
    a = Solution()
   #  %time a.search(temp, 9)
   #  %time a.search2(temp, 9)

    # CPU times: user 32 µs, sys: 1 µs, total: 33 µs
    # Wall time: 36.7 µs
    # CPU times: user 7 µs, sys: 1 µs, total: 8 µs
    # Wall time: 11.9 µs