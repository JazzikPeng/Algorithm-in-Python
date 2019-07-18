# Dynamic Programming Problem
# 写出动态规划的表达式
# f[i][j] = min(f[i-1,j], f[i-1,j-1]) + triangle[i][j]
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Creat n x n array
        n = len(triangle)
        f = [[float('inf') for x in range(n)] for y in range(n)]
        f[0][0] = triangle[0][0]
        print(len(f), len(f[0]))
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    f[i][j] = f[i-1][j] + triangle[i][j]
                # elif j == n - 1:
                #     f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
                else:
                    f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
        return min(f[-1])

    # Use O(n) Space solution
    def minimumTotal_On(self, triangle: List[List[int]]) -> int:
        # Creat n x n array
        n = len(triangle)
        if n < 2:
            return triangle[0][0]
        prev = [float('inf') for x in range(n)]
        curr = [float('inf') for x in range(n)]
        prev[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                # print('i, j', i, j)
                # print('prev', prev)
                if j == 0:
                    curr[j] = prev[j] + triangle[i][j]
                    # print(curr[j])
                elif j == i :
                    curr[j] = prev[j-1] + triangle[i][j]
                    # print('prev', prev)
                else:
                    curr[j] = min(prev[j], prev[j-1]) + triangle[i][j]
                # print(curr)
            
            prev = curr.copy()
        return min(curr)

s = Solution()
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(s.minimumTotal_On(t))