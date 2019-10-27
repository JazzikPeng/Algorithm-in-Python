# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        temp = self.binaryTreePaths(root)
        return sum([int(x) for x in temp])
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        path = [] 
        self.printPathsRec(root, path, 0) 
        return self.paths
  

    def printPathsRec(self, root, path, pathLen): 

        # Base condition - if binary tree is 
        # empty return 
        if root is None: 
            return

        # add current root's data into  
        # path_ar list 

        if(len(path) > pathLen):  
            path[pathLen] = root.val 
        else: 
            path.append(root.val) 

        pathLen = pathLen + 1

        if root.left is None and root.right is None: 
            self.saveArray(path, pathLen)
        else: 
            self.printPathsRec(root.left, path, pathLen) 
            self.printPathsRec(root.right, path, pathLen) 
    
    def saveArray(self, ints, len): 
        temp =""
        for i in ints[0 : len]: 
            temp += str(i) 
        self.paths.append(temp)