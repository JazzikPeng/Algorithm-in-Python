# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.results = []
        self.traverse(root)
        return self.results
    
    def traverse(self, root):
        if root is None:
            return 
        self.traverse(root.left)
        self.traverse(root.right)
        self.results.append(root.val)
 

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Post order is a reversed pre-order going to the right. 
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        stack.append(root)
          
        if root==None:
            return res
        while len(stack)>0:
            node = stack.pop()
            res.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return res[::-1]