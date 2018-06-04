
# coding: utf-8

# In[95]:


# Definition for a binary tree node.
# Leetcode 105 Construct Binary Tree from Preorder and Inorder Traversal 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[106]:


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, 0, len(inorder)-1, preorder, inorder);
    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        # Boundary
        if(preStart > len(preorder) - 1) or (inStart > inEnd):
            return None
        # Root
        root = TreeNode(preorder[preStart])
        inIndex = 0
        for i in range(inStart, inEnd+1):
            if(inorder[i] == root.val):
                inIndex =i
                break
        # inIndex -1 for inorder, becuase we found the root,then anything on left is the left child
        root.left = self.helper(preStart+1, inStart, inIndex-1, preorder, inorder)
        root.right= self.helper(preStart+inIndex-inStart+1 , inIndex+1, inEnd, preorder, inorder)
        return root

if __name__ == '__main__':
    b = Solution()
    print(b.buildTree([3,9,15,7,20], [15,9,7,3,20]).val)

