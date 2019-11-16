class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        if len(s) == 1:
            if int(s[0]) != 0:
                return 1
            else:
                return 0
        total_ways = [None] * (len(s))
        if int(s[0])==0:
            return 0        
        if int(s[1]) == 0 and int(s[0]) > 2:
            return 0
        total_ways[0] = 1
        if int(s[0]) == 1:
            if int(s[1])==0:
                total_ways[1] = 1
            else:
                total_ways[1] = 2
        elif int(s[0]) == 2:
            if int(s[1])==0: 
                total_ways[1] = 1
            elif int(s[1])<=6:
                total_ways[1] = 2
            else:
                total_ways[1] = 1
        elif int(s[0]) > 2:
            total_ways[1] = 1



        for i in range(2, len(s)): # assume have solution
            if int(s[i]) == 0: # '230'
                if int(s[i-1]) > 2 or int(s[i-1]) == 0: # '2231230'
                    return 0 # No solution
                else:
                    total_ways[i] = total_ways[i-2] 
            elif int(s[i-1]) == 0:
                total_ways[i] = total_ways[i-1]
            else: 
                if int(s[i-1]) < 2 or (int(s[i-1]) == 2 and int(s[i]) <=6):# '211' or '226'
                    total_ways[i] = total_ways[i-1] + total_ways[i-2]
                elif int(s[i-1]) > 2 or (int(s[i-1]) == 2 and int(s[i]) > 6):# '271' '227'
                    total_ways[i] = total_ways[i-1] 
        return total_ways[-1]