class Solution:
    def myAtoi(self, str: str) -> int:
        result = ''
        counter = 0
        s = str
        if len(s) < 1:
            return 0
        nega_flag = False
        sign_count = 0
        for i in range(len(s)):
            if s[i] == ' ' and counter == 0:
                continue
            if s[i].isdigit() == False and counter >= 1:
                break
            if s[i] != ' ':
                counter += 1

            if s[i] == '-' and len(result) == 0:
                nega_flag = True
                sign_count += 1
                continue
            if s[i] == '+' and len(result) == 0:
                sign_count += 1
                continue
            if s[i].isdigit():
                result += s[i]
            else:
                break
        if len(result) == 0 or sign_count > 1:
            return 0
        if abs(int(result)) >= 2147483648:
            if nega_flag:
                result = 2147483648
            else:
                result = 2147483648 - 1
        if nega_flag:
            return -int(result)
        else:
            return int(result)
