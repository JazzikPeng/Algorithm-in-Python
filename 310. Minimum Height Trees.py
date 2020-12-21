class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Max number of root is 2
        if n <= 2:
            return [i for i in range(n)]
        neighbors = [set() for i in range(n)]
        
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        # Find initial first layer nodes
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        # Trim the leaves
        rest_nodes = n
        while rest_nodes > 2:
            rest_nodes -= len(leaves)
            next_leaves = []
            for l in leaves:
                neighbor = neighbors[l].pop()
                neighbors[neighbor].remove(l)
                if len(neighbors[neighbor] ) == 1: # 
                    next_leaves.append(neighbor)
            leaves = next_leaves
        return leaves
        
        
        
        
        