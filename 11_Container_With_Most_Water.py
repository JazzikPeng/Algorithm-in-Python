
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        if r <= 0:
            return None
        max_Water = 0
        while l < r:
            h = min(height[l], height[r])
            max_Water = max(max_Water, h*(r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_Water
