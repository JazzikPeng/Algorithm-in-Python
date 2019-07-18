from typing import List
import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        re = []
        for i in range(0, rowIndex+1):
            re.append(self.nCr(rowIndex, i))
        return re

    def nCr(self, n, r):
        numerator = math.factorial(n)
        denomenator = math.factorial(n-r) * math.factorial(r)
        return int(numerator / denomenator)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t=[[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1,i):
                t[i][j] =t[i-1][j-1]+t[i-1][j]
                
        return t[rowIndex]