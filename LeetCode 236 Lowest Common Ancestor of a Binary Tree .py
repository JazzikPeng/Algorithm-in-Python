# LeetCode 236 Lowest Common Ancestor of a Binary Tree 
# coding: utf-8

# In[4]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # Divide 
        left = self.lowestCommonAncestor(root.left, p, q)
        right= self.lowestCommonAncestor(root.right, p, q)
        
        # Conquer
        # both left and right have value
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
        
            
        

