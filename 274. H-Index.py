class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        h = 1
        for i in citations:
            if i >= h:
                pass
            else:
                return h -1
            h += 1
        return h - 1