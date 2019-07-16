
class Solution:
    def findPairs(self, nums, k: int) -> int:
        result=0
        if k<0:
            return 0
        elif k==0:
            dic=collections.Counter(nums)
            for i in dic.values():
                if i!=1:
                    result+=1
        else:
            num=set(nums)
            for i in num:
                if i+k in num:
                    result+=1
        return result