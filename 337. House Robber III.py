# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.dic = {}
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        if root in self.dic:
            return self.dic[root]
        
        rob1 = self.rob(root.left) + self.rob(root.right) 
        rob2 = root.val 
        if root.left:
            rob2 += self.rob(root.left.left) + self.rob(root.left.right) 
        if root.right: 
            rob2 += self.rob(root.right.right) + self.rob(root.right.left)
        re = max(rob1, rob2)
        self.dic[root] = re
        return re
        

        
# 状态 f 是这个根能找到的最大值 f(root)
# 状态转移方程：f(root) = max(f(root.left) + f(root.right) , root.val + f(root.left.left) + f1 + f2 ...)
# base case: if root is None; return root.val


