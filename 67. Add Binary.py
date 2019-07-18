class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = bin(int(a,2) + int(b,2))[2:]
        return a