class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        cur_min = None
        if k == 1:
            return max(nums)
        stack = []
        for i in nums:
            # print(stack)
            if len(stack) < k:
                stack.append(i)
            if cur_min:
                if i > cur_min:
                    stack.remove(cur_min)
                    stack.append(i)
                    cur_min = min(stack)
            if len(stack) == k:
                cur_min = min(stack)

        # print(stack)
        return min(stack)