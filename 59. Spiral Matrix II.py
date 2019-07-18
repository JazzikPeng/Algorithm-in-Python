from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create a nxn matrix
        if n < 2:
            return [[1]]
        max_ = n*n
        mat = [[None for x in range(n)] for y in range(n)]
        top, bot, left, right = 0, n-1, 0, n-1
        layer = 0
        count2 = 1
        while top < bot and left <  right:
            count = count2
            print(count, top, bot)
            for i in range(n-1):
                mat[top][left+i] = count
                mat[top+i][right] = count + n - 1
                mat[bot][right-i] = count + 2*(n-1)
                mat[bot-i][left] = count + 3*(n-1)
                count += 1
            count2 = count2 + 4*(n-1)
            n = n - 2
            layer += 1
            top += 1
            left += 1
            bot -= 1
            right -= 1
            if top==bot and left==right:
                print('HERE')
                mat[top][bot] = max_

                break
        return mat    



s = Solution()
print(s.generateMatrix(2))