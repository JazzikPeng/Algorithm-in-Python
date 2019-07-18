class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret_val=str(bin(n)[2:].zfill(32))[::-1]
        return (int(ret_val,2))

s = Solution()
print(s.reverseBits(43261596))