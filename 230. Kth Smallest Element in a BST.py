# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = 0
        self.t = k
        self.r = None
        r = self.inorder(root)
        return self.r
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.counter += 1

        if self.counter == self.t:
             self.r  = root.val
             return 
        self.inorder(root.right)


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        counter = 0
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            counter+=1
            if counter == k:
                return node.val
            node = node.right