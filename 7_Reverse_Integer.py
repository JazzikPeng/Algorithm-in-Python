class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            raise ValueError
        try:
            r = int(str(x)[::-1])
        except:
            r = -int(str(-x)[::-1])
        if r > 2**31 -1 or r < -2**31:
            return 0
        return r