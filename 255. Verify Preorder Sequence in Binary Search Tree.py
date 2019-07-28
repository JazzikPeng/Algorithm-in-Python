class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack, max_val = [], float('-inf')
        for i in preorder:
            while stack and stack[-1] < i:
                max_val = stack.pop()
            if i > max_val:
                stack.append(i)
            else:
                return False
        return True