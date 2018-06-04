# Binary Tree levelorder traversal
# Breadth-First Search
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = {}
        return self.helper(root, 0, dic)
    def helper(self, root, l, level):
        if root == None:
            return []
        if l in level:
            level[l].append(root.val)
        else:
            level[l] = [root.val]

        self.helper(root.left, l+1, level)
        self.helper(root.right, l+1, level)
        
        ret = [None] * len(level)
        for i in level:
            ret[i] = level[i]
        return ret

class Solution:
    def levelOrder_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        current_level = [root]
        ret = []
        if root == None:
            return ret
        while current_level:
            next_level, vals = [],[]
            for node in current_level:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            ret.append(vals)
        return ret

if __name__ == '__main__':
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)
    a.left.right= TreeNode(5)
    b = Solution()
    print(b.levelOrder(a))