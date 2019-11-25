class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations and len(citations)==0:
            return 0
        
        l, r=  0, len(citations) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if citations[mid] < len(citations) - mid: # this represents the number of paper > current h
                l = mid + 1
            elif citations[mid] > len(citations) - mid:
                r = mid -1
            else:
                return citations[mid]
        
        return len(citations) - l