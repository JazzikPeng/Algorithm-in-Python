# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




pInorder = 0
pPostorder = 0
class Solution:
    def set_pInorder(self,n):
        global pInorder    # Needed to modify global copy of globvar
        pInorder = n
    def set_pPostorder(self,n):
        global pPostorder
        pPostorder = n
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.set_pInorder((len(inorder) - 1))
        self.set_pPostorder((len(postorder) - 1))
        return self.helper(inorder, postorder, None)
    
    def helper(self, inorder, postorder, end):
#         print("pInorder: ", pInorder)
#         print("pPostorder: ", pPostorder)
#         print("Inorder: ", inorder[0:pInorder+1])
#         print("postorder: ", postorder[0:pPostorder+1])
#         print("end.val: ", end if end==None else end.val)
        if(pPostorder < 0):
            return None
        # The Last element in pPostorder is the root
        root = TreeNode(postorder[pPostorder])
#         print("root.val: ", root.val)
        self.set_pPostorder(pPostorder-1)
        if (inorder[pInorder] != root.val):
            root.right = self.helper(inorder, postorder, root)
#         print("pInorder: ", pInorder)
#         print("==========================")
        self.set_pInorder(pInorder-1)
        if(end==None or inorder[pInorder] != end.val):
            root.left = self.helper(inorder, postorder, end)
        return root


if __name__ == '__main__':
    b = Solution()
    print(b.buildTree([9,3,15,20,7], [9,15,7,20,3]).val)