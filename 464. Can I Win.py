class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False
        
        if desiredTotal <= 0:
            return True
        
        bool_array = [i for i in range(1,maxChoosableInteger+1)]
        
        self.cache = {}
        
        return self.minimax(desiredTotal,bool_array)
    
    def minimax(self,desiredTotal,visited):
        
        if tuple(visited) in self.cache:
            return self.cache[tuple(visited)]
        if desiredTotal <= 0:
            return False
        for i in range(len(visited)):
            temp = visited[i]
            newV = visited[:i] + visited[i+1:]
            if not self.minimax(desiredTotal-temp,newV):
                self.cache[tuple(visited)] = True
                return True
        self.cache[tuple(visited)] = False
        return False

s = Solution()
print(s.canIWin(10, 3))
print(s.cache)