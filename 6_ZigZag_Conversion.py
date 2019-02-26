class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        if numRows<1:
            raise ValueError
        if s is None:
            raise ValueError
        if len(s) < numRows:
            return s
        if len(s) < 1:
            raise ValueError
        tmp = []
        i = 0
        while i < len(s):
            j = i+2*(numRows-1)
            tmp.append(s[i:j])
            i+=2*(numRows-1) 
        result = {}
        for s in tmp:
            for i in range(len(s)):
                if i < numRows:
                    try:
                        result[i]+=s[i]
                    except:
                        result[i]=s[i]
                else:
                    j = numRows-1 - i % (numRows-1)
                    result[j] += s[i]
        re = ''
        for key, val in result.items():
            re+=val
        return re