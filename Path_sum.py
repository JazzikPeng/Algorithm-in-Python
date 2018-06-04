# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Path Sum
array = []
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """ 



    # Best Solution:
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right:
            return s == root.val 
        elif not root.left:
            return self.hasPathSum(root.right, s-root.val)
        elif not root.right:
            return self.hasPathSum(root.left, s-root.val)
        else:
            return self.hasPathSum(root.right, s-root.val) or self.hasPathSum(root.left, s-root.val) 


    # Another solution
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        return False
        
    def traverse(self, root, path_sum, sum):
        if root is None:
            return 
        path_sum += root.val
        #print(path_sum, sum)
        if path_sum == sum and self.isLeaf(root):
            array.append(path_sum)
            return True
        else:
            self.traverse(root.left, path_sum, sum)
            self.traverse(root.right, path_sum, sum)
       # return False
     
        
    def hasPathSum(self, root, sum):
        if not root:
            return False
        self.traverse(root, 0, sum)
        print(array)
        if sum in array:
            array.clear()
            return True
        return False
        
        

if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
#     a.right = TreeNode(3)
#     a.left.left = TreeNode(4)
#     a.left.right= TreeNode(5)
    b = Solution()
    print(b.hasPathSum(a, 3))
    
    b = TreeNode(1)
    b.left = TreeNode(-2)
    b.right = TreeNode(-3)
    b.left.left = TreeNode(1)
    b.left.right= TreeNode(3)
    b.left.left.left = TreeNode(-1)
    b.right.left = TreeNode(-2)
    c = Solution()
    print(c.hasPathSum(b, 4))