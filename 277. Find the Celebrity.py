# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 遍历一遍到最后一位数, 这一步为什么? 这里的目的是一直遍历到最底层的认识关系嘛，那如果 1->5, 5->3 怎么办？
        # 因为所有人都认识 这个celebrity，所以一定会走到他这里除非没有celebrity
        s = 0
        for i in range(n):
            if i!=s and knows(s, i):
                s = i
        for j in range(n):
            if s!=j:
                if knows(j, s) and not knows(s, j):
                    pass
                else:
                    return -1
        return s
        