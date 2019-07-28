# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return None, None
        elif root.val <= V:
            s = self.splitBST(root.right, V)
            root.right = s[0]
            return root, s[1]
        else:
            s = self.splitBST(root.left, V)
            root.left = s[1]
            return s[0], root 