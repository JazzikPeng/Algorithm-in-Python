class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        
        arr_of_nums = [i for i in range(1, maxChoosableInteger+1)]
        
        self.cache = {}
        return self.minMax(desiredTotal, arr_of_nums)

    def minMax(self, desiredTotal, visited):
        if tuple(visited) in self.cache:
            return self.cache[tuple(visited)] 
        if desiredTotal <= 0:
            return False
        for i in range(len(visited)):
            newGoal = desiredTotal - visited[i]
            newVisited = visited[:i] + visited[i+1:]
            if not self.minMax(newGoal, newVisited):
                self.cache[tuple(visited)] = True
                return True
        self.cache[tuple(visited)] = False
        return False


s = Solution()
print(s.canIWin(6, 16))
print(s.cache)
