# Binary Tree inorder traversal
# Left Subtree -> Root -> Right Subtree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None
        
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
    
if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.left = TreeNode(3)
    b = Solution()
    print(b.inorderTraversal(a))