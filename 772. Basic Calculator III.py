class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        re, _ ,_= self.get_num_in(s,0,[], 0)
        return int(float(re))

    def compute(self, t):
        r = eval("".join(t))
        return int(float(r))
    
    def get_num_in(self, s, num=0, stack=[], count_recur=0):
        i = 0 
        while i < len(s):
            if s[i] == '(':

                t1, t2, count_recur = self.get_num_in(s[i+1:], num, stack=[], count_recur=0)
                stack.append(t1)
                i += t2 + count_recur*2 - 1
                count_recur=0
            elif s[i] == ')':
                count_recur=count_recur+1
                return str(self.compute(stack)), len(stack), count_recur
            elif s[i].isdigit():
                j = i 
                r = '' 
                while j < len(s):
                    if s[j].isdigit():
                        r+=s[j]
                    else:
                        break
                    j+=1
                i = j - 1
                stack.append(r)
            else:
                stack.append(s[i])
            i += 1

        return str(self.compute(stack)), len(stack), count_recur
        
        

sol = Solution()
ss = "((3)) + 4"
"2*(5+5*2)/3+(6/2+8)"
print(eval(ss))
print(sol.calculate(ss))       

