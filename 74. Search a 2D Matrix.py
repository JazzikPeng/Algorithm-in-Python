class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # This is basically a binary search 
        # Transfer to 2D array
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)
        l, r = 0 , len(arr)
        if r==1 and arr[0]==target:
            return True
        if r==1 and arr[0]!=target:
            return False
        if r==0:
            return 
        
        while l + 1 < r:
            mid = (l+r) // 2
            if arr[mid] > target:
                r = mid
            elif arr[mid] < target:
                l = mid 
            else:
                return True
        return arr[l]==target


