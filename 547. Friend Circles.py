class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        row = len(M)
        col = len(M[0])
        assert row == col
        
        uf = UnionFind(row)        
        for i in range(row):
            for j in range(col): # Update only upper right half
                if M[i][j] == 1 and i!=j:
                    #print(i,j)
                    uf.union(i, j)
                    #print(uf.parent)
        
        parent= []
        for node in uf.parent:
            root = uf.find(node)
            if root not in parent:
                parent.append(root)
        return len(parent)
                
        
class UnionFind:
    """
    Class that implements the union-find method
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u1, u2):
        root1 = self.find(u1)
        root2 = self.find(u2)
        if root1 == root2:
            return # Already in the same disjointed set
        if self.rank[root1]  > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

            # Use rank 