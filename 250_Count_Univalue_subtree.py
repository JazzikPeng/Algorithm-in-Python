# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        counter = 0
        counter,_ = self.helper(root, counter);
        return counter
    
    def helper(self, root, res):
        if root == None:
            return res, True
        res, left = self.helper(root.left,res)
        res, right= self.helper(root.right,res)
        if(left and right):
            if root.left!=None and root.val != root.left.val:
                return res, False
            if root.right!=None and root.val != root.right.val:
                return res, False
            res = res+1
           # t.append(res)
            return res,True;
        return res, False
            

if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(1)
    a.right=TreeNode(5)
    a.left.left = TreeNode(5)
    a.left.right= TreeNode(5)
    a.right.right=TreeNode(5)
#     a.right = TreeNode(3)
#     a.left.left = TreeNode(4)
#     a.left.right= TreeNode(5)
    b = Solution()
    print(b.countUnivalSubtrees(a))