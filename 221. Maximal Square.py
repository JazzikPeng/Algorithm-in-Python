class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Start from matrix[1, 1]
        max_area = 0
        r= len(matrix)
        if r==0:
            return 0
        c = len(matrix[0])
        if r < 2 or c < 2:
            for i in range(r):
                for j in range(c):
                    if matrix[i][j]=='1':
                        return 1
        dp = [[0 for x in range(c)] for y in range(r)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='1':
                    try:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    except:
                        dp[i][j] = 1
                    if dp[i][j] > max_area:
                        max_area = dp[i][j]
        return max_area**2
    
s = Solution()
input =[["1"]]
print(s.maximalSquare(input))