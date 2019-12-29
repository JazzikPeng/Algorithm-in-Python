class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.i, self.j = 0, 0
        self.v1, self.v2 = v1, v2

    def next(self):
        """
        :rtype: int
        """
        ans = -1
        if self.i < len(self.v1):
            self.i += 1
            ans = self.v1[self.i-1]
        elif self.j < len(self.v2):
            self.j += 1
            ans = self.v2[self.j-1]
    
        self.i, self.j = self.j, self.i
        self.v1, self.v2 = self.v2, self.v1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i + self.j < len(self.v1) + len(self.v2):
            return True
        return False        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

# [0, 0]
# 偶数: 不前进
# 奇数: 前进
# -1：结束