"""
BackTracking,
You dont have track the path.
"""
# Do not Track the path
class Solution:
    def totalNQueens(self, n: int) -> int:
        paths = []
        def isValid(r, c, cur_path): 
            """
            cur_path: existing queens
            """
            if r in cur_path:
                return False
            # diag situation
            for i, j in enumerate(cur_path): # i is col, j is row
                if abs(r - j) == abs(c - i): # In diag
                    return False
            return True
        
        def backTracking(c, cur_path=[]):
            if c == n: # find all solution
                paths.append(cur_path)
                return 
            for r in range(n):
                if isValid(r, c, cur_path): # Cur position
                    backTracking(c+1, cur_path+[r]) # This creates a new copy of cur_path, the previous path is kept.
        backTracking(0, [])
        return len(paths)
        
            