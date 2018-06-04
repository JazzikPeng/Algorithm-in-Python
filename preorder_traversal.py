# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Binary Tree Preorder traversal
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        stack.append(root)
        
        if (root == None):
            return ret
        
        while(len(stack)>0):
            node = stack.pop()
            ret.append(node.val)
            if(node.right != None):
                stack.append(node.right)
            if(node.left != None):
                stack.append(node.left)
        return ret


    # Recursive Solution
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


if __name__ == '__main__':
    a = TreeNode(1)
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)
    b = Solution()
    print(b.preorderTraversal(a))