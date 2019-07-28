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



# Python program to do inorder traversal without recursion 
  
# A binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# Iterative function for inorder tree traversal 
def inOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    stack = [] # initialize stack 
    done = 0 
    
    while True: 
          
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            stack.append(current) 
          
            current = current.left  
  
          
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        elif(stack): 
            current = stack.pop() 
            print(current.data, end=" ") # Python 3 printing 
          
            # We have visited the node and its left  
            # subtree. Now, it's right subtree's turn 
            current = current.right  
  
        else: 
            break
    
  
# Driver program to test above function 
  
""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """
  
root = Node(3) 
root.left = Node(1) 
root.right = Node(4) 
root.right.left = Node(2) 
  
in_traversal = [1,3,2,4]
first = None
second = None
prev = None
curr = None
for i in range(1,len(in_traversal)):
    curr = in_traversal[i]
    prev = in_traversal[i-1]
    # print(curr, prev)
    if curr < prev and first is None:
        first = prev
    if curr < prev and first is not None:
        second = curr

print(first, second)

