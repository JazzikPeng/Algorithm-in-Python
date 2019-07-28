# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Do in order traversal. The in order traversal is monotonically increase
# O(1) Space, can not use iterative method or recursive solution, both use space

# class Solution(object):
#     first = TreeNode(None)
#     second = TreeNode(None)
#     prev = TreeNode(None)

#     def recoverTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: None Do not return anything, modify root in-place instead.
#         """
#         # Recursion Method
#         if root is None:
#             return 
        

#     def helper(self, curr):
#         if curr is None:
#             return 
#         helper(curr.left)
#         if prev is not None and prev.val >= curr.val: 
#             # have mistake first is the prev node, second is the curr node
            

# Morris Traversal O(1) solution
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = TreeNode(None)
        second = TreeNode(None)
        prev = TreeNode(-float('inf'))
        firstTime = True
        # Recursion Method
        while root is not None:
            if root.left is not None:
                temp = root.left
                while temp.right is not None and temp.right is not root:
                    temp = temp.right
                if temp.right is None:
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    if prev.val > root.val and firstTime:
                        first = prev
                        firstTime = False 
                    if prev.val > root.val and not firstTime:
                        second = root
                    prev = root
                    root = root.left
            else:
                # visit root.val
                if prev.val > root.val and firstTime:
                    first = prev
                    firstTime = False 
                if prev.val > root.val and not firstTime:
                    second = root
                prev = root
                root = root.right
            # Now we can swap
        if first is not None and second is not None:
            val = first.val
            first.val = second.val
            second.val = val
    


class Solution(object):
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        point = root
        last = None  # last point
        big = None
        small = None
        while point:
            if point.left is None:
                # visit
                if last and last.val > point.val:
                    if big is None:
                        big = last
                    small = point
                last = point
                # end visit
                point = point.right
            else:
                pre = point.left
                while pre.right and pre.right is not point:
                    pre = pre.right
                if pre.right is None:
                    pre.right = point
                    point = point.left
                else:
                    pre.right = None
                    # visit
                    if last and last.val > point.val:
                        if big is None:
                            big = last
                        small = point
                    last = point
                    # end visit
                    point = point.right
        big.val, small.val = small.val, big.val