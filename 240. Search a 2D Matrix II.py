class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        h = len(matrix)
        w = len(matrix[0])

        # start our "pointer" in the bottom-left
        r = h-1
        c = 0

        while c < w and r >= 0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else: # found it
                return True
        return False