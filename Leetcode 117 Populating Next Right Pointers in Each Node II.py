
# coding: utf-8

# In[126]:


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# Time = O(n)
# Space = O(1)
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        print(root.val)
        if root == None:
            return root
        if root.left == None and root.right == None:
            root.next = None
            # return root
            return 
        head = None
        cur = root
        pre = None
        # print(cur.val)

        while(cur!= None):
            while(cur!=None):
                if cur.left !=None:
                    if pre!=None:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                if cur.right !=None:
                    if pre!=None:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                cur = cur.next
            cur = head
            pre = None
            head = None
        # return root

