# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        left, right = 1, n
        
        while right >= left:
            mid = (left+right) // 2
            gus = guess(mid)
            if gus == 0:
                return mid
            if gus == -1:
                right = mid-1
            elif gus == 1:
                left = mid + 1
        return mid
            