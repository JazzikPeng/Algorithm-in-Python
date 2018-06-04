# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Binary Tree postorder traversal
# Left Subtree -> Right Subtree -> Root
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        stack2 = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                stack2.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        while stack2:
            temp = stack2.pop()
            result.append(temp.val)
        return result

    # Recursion:
    def postorderTraversal(self, root):
        res = []
        if root == None: 
            return res
        self.helper_p(res,root)
        return res
    def helper_p(self,res, root):
        if(root == None): 
            return
        self.helper_p(res, root.left)
        self.helper_p(res, root.right)
        res.append(root.val)

            
    

if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)
    b = Solution()
    print(b.postorderTraversal(a))