class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Find JFK
        from collections import defaultdict
        self.flightMap = defaultdict(list)
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        
        self.visitBitmap = {}
        for origin, itinerary in self.flightMap.items():
            itinerary.sort()
            self.visitBitmap[origin] = [False] * len(itinerary)
            
        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        res = self.backtracking('JFK', route)
        if res:
            return self.result
        
    def backtracking(self, origin, route):
        if len(route) == self.flights + 1: # End
            self.result = route
            return True
        
        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True
        return False
            
# Eulerian path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Find JFK
        from collections import defaultdict
        self.flightMap = defaultdict(list)
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        
        for origin, itinerary in self.flightMap.items():
            itinerary.sort(reverse=True) # reverse the search. Becuase we going backward.
        
        self.results = []
        self.dfs('JFK')
        return self.results[::-1]
        
        
    def dfs(self, origin):
        destList = self.flightMap[origin]
        while destList:
            nextDest = destList.pop()
            self.dfs(nextDest)
        self.results.append(origin)
            
        
        
        