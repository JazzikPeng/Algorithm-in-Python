class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        re = []
        for p in positions:
            r, c = p[0], p[1]
            overlap = []
            # print(r, c, uf.isValid(r*n + c-1))
            if r - 1 >= 0 and uf.isValid((r-1)*n + c):
                overlap.append((r-1)*n + c)
            if r + 1 < m and uf.isValid((r+1)*n + c):
                overlap.append((r+1)*n + c)
            if c - 1 >= 0 and uf.isValid(r*n + c-1):
                overlap.append(r*n + c - 1)
            if c + 1 < n and uf.isValid(r*n + c + 1):
                overlap.append(r*n + c + 1)
            parent_idx = r*n + c
            uf.setParent(parent_idx)
            # print(overlap, parent_idx, uf.parent)
            for i in overlap:
                uf.union(i, parent_idx)
            re.append(uf.count)
        # print(uf.parent)
        return re
        
        
        
class UnionFind:
    """
    UnionFind with Path Compression
    """
    def __init__(self, n):
        self.count = 0  # Number of connected Components
        self.parent = [-1] * n
        self.rank = [0] * n
    
    def isValid(self, idx):
        # -1 is not valid
        return self.parent[idx] >= 0
    
    def setParent(self, idx): 
        if self.parent[idx] == -1: # This idx is init as parent the first time.
            self.parent[idx] = idx
            self.count += 1

    def find(self, v): # Path compression
        if self.parent[v] != v: # if parent is not itself.
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u1, u2):
        root1 = self.find(u1)
        root2 = self.find(u2)
    
        if root1 == root2:
            return # Already in the same union
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
        self.count -= 1
        
                
        