# Max. depth of a tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Level Order Traversal, put none if there is no node to make a balanced Tree
        current_level = [root]
        ret = []
        if root == None:
            return True
        while current_level:
            next_level, vals = [],[]
            for node in current_level:
                if node:
                    vals.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    else:
                        next_level.append(None)
                    if node.right:
                        next_level.append(node.right)
                    else:
                        next_level.append(None)
                else:
                    vals.append(None)
            current_level = next_level
            ret.append(vals)
        
        #print(ret)
        # Now we have each level's node, check if they are symmetric
        for i in ret[1:]:
            j = len(i) 
            if j % 2 !=0:
                return False
            else:
                for n in range(int(j/2)):
                    if i[n]!=i[-n-1]:
                        #print(i[n], i[-n-1])
                        return False
        return True

    # Recursiv Method
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right or left.val !=right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
 
if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(2)
#    a.left.left = TreeNode(3)
    a.left.right=TreeNode(3)
#     a.right.left=TreeNode(4)
    a.right.right= TreeNode(3)
    b = Solution()
    print(b.isSymmetric(a))