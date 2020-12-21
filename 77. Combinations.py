from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k+1)) + [n + 1]
        output, j = [], 0
        while j < k:
            output.append(nums[:k])
            j = 0 
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
        return output
        
        
s = Solution()
print(s.combine(4, 3))

s = {'aa':'b'}
print(s.pop('aa'))