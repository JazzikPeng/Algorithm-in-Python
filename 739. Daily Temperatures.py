class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        re = [0] * len(T)
        for i in range(len(T)):
            t = T[i]
            if not stack or t < T[stack[-1]]:
                stack.append(i)
            else:
                while stack and t > T[stack[-1]]:
                    s = stack.pop()
                    re[s] = i - s
                stack.append(i)
        return re
                    
            