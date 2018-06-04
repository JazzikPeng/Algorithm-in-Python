
# coding: utf-8

# In[ ]:


# 297 Serialize and Deserialize Binary Tree


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root == None:
                result.append('null')
                return
        # print(root.val)
            result.append(root.val)
            helper(root.left)
            helper(root.right)
        result = []
        helper(root)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper2(data):
            index = len(temp)
            val = data[index]
            # print(index)
            temp.append(1)
            # print(data)
            if val == 'null':
                return None
            root = TreeNode(val)
            # print(root.val)
            root.left = helper2(data)
            root.right = helper2(data)
            return root
        if data == None:
            return
        # Temp list are used for counter
        temp = []
        root = helper2(data)
        return root


# In[469]:


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
# # root.left.left = TreeNode(6)


# In[470]:


b = Codec()
data = b.serialize(root)
root = b.deserialize(data)
print(root.right.left.val)


# In[471]:


root.right.left.val


# In[472]:


# solution 2
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        print(vals)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


# In[473]:


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

b = Codec()

b.serialize(root)
