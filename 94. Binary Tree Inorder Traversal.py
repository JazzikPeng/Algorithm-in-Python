# #Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.inorder = [] 
    # A function to do inorder tree traversal 
    def inorderTraversal(self, root):
        self.helper(root)
        return self.inorder
    
    def helper(self, root):
        if root:
            if root.left:
                self.helper(root.left)
            self.inorder.append(root.val)
            if root.right:
                self.helper(root.right)
            