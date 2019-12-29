class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        nodes = set()
        
        for s in seqs:
            for i in range(len(s)):
                nodes.add(s[i])
                if i > 0:
                    parents[s[i]].add(s[i-1])
                if i < len(s) - 1:
                    children[s[i]].add(s[i+1])
        potential_parent = [n for n in nodes if not parents[n]]
        
        indegree = len(potential_parent) # Count is the in-degree
        ans = [] # ans is the final result 
        
        while indegree == 1: # Indegree need to equal one
            cur_parent, count = potential_parent.pop(), indegree - 1
            ans.append(cur_parent)
            nodes.remove(cur_parent)
            for n in children[cur_parent]:
                parents[n].remove(cur_parent)
                if not parents[n]:
                    potential_parent.append(n)
                    indegree += 1
        return True if not nodes and ans==org else False
        