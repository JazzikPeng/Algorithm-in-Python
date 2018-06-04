
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
# Leetcode 105 Construct Binary Tree from Preorder and Inorder Traversal 
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# In[5]:


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root==None:
            return
        if root.left != None:
            root.left.next  = root.right
        if root.next!= None and root.right!=None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
    
    # space o(1) 
    def connect(self, root):
        start = root
        while(start!=None):
            cur = start
            while(cur!=None):
                if cur.left!=None:
                    cur.left.next = cur.right
                if cur.right!=None and cur.next!=None:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
        
    


# In[4]:





# In[2]:




