# Binary_Search Method
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row,col = len(matrix),len(matrix[0])
        l,r = matrix[0][0],matrix[-1][-1]
        while l + 1 < r:
            mid = l + (r - l) / 2
            mid = int(mid)
            if not self.check(matrix,mid,k):
                l = mid
            elif self.check(matrix,mid,k):
                r = mid
        
        if self.check(matrix,l,k):
            return l
        if self.check(matrix,r,k):
            return r
    
    def check(self,matrix,target,k):
        res = 0
        row,col = len(matrix),len(matrix[0])
        for i in range(row):
            idx = self.find_last_noLarger(matrix[i],target)
            res += idx + 1
        
        return res >= k
    
    def find_last_noLarger(self,nums,target):
        l,r = 0,len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            mid = int(mid)
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[r] <= target:
            return r
        if nums[l] <= target:
            return l
        return -1