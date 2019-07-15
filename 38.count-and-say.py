#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        prev = [1]
        if n == 1:
            return '1'
        for i in range(1, n):
            prev = self.seq_speaker(prev)
        return ''.join([str(x) for x in prev])
        # if n == 1:
        #     re = [1]
        # i = 1
        # while i <= n:
        #     re = []
        #     for j in range(i):
                
            
        #     i += 1

    def seq_speaker(self, arr):
        if arr == [1]:
            return [1, 1]
        count = 1
        re = []
        prev = arr[0]
        for i in range(1, len(arr)+1):
            try:
                if arr[i] == prev:
                    count+=1
                if arr[i] != prev:
                    re.extend([count, prev])
                    prev = arr[i]
                    count = 1
            except:
                re.extend([count, prev])
        return re
            

s = Solution()
print(s.countAndSay(5))
print(s.seq_speaker([1,2]))