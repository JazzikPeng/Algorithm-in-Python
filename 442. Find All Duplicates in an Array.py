from collections import *
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = []
        cnt = Counter()
        for i in nums:
            if cnt[i]>0:
                dup.append(i)
            cnt[i]+=1
        return dup

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        unique = set()
        duplicates = []
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                duplicates.append(num)
        return duplicates