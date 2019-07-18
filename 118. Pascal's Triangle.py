from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        re = []
        if numRows >= 1:
            re.append([1])
        if numRows >= 2:
            re.append([1, 1])
        i = 3
        while i <= numRows:
            print(re)
            tmp = [x+y for x,y in zip(re[-1][:-1], re[-1][1:])]
            tmp.insert(0, 1)
            tmp.insert(i, 1)
            re.append(tmp)
            i += 1
        
        return re

s = Solution()
print(s.generate(5))