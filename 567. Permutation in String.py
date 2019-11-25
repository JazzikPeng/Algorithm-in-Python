class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Slicing window hash map
        if len(s1) > len(s2):
            return False
        s1map = [0 for x in range(26)]
        s2map = [0 for x in range(26)]
        # init hashmap for s1, s2
        for i in range(len(s1)):
            a ,b = s1[i], s2[i]
            s1map[ord(a)-ord('a')]+=1
            s2map[ord(b)-ord('a')]+=1
        # Create hashmap for s2
        for i in range(len(s2) - len(s1)):
            if self.compHash(s1map, s2map):
                return True
            s2map[ord(s2[i])-ord('a')] -= 1
            s2map[ord(s2[i+len(s1)])-ord('a')] += 1
        
        return self.compHash(s1map, s2map)

    def compHash(self, h1, h2):
        if h1==h2:
            return True
        else:
            return False

from collections import *
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window solution
        dic = Counter(s1)
        win = {}
        if len(s1) > len(s2):
            return False
        for s in s2[:len(s1)]:
                win[s] = win.get(s, 0) + 1

        for i in range(len(s1), len(s2)):
            if win == dic:
                return True
            win[s2[i - len(s1)]] -=  1
            if win[s2[i - len(s1)]]<= 0:
                win.pop(s2[i - len(s1)])
            win[s2[i]] = win.get(s2[i], 0) + 1
        
        if win == dic:
            return True
        return False


a = "ab"
b = "eidbaoo"

s = Solution()
print(s.checkInclusion(a, b))