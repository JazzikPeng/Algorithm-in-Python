# Double For Loop
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindromic(input_str):
            if input_str == input_str[::-1]:
                return True
            else:
                return False
        if s is None:
            raise ValueError
        if len(s) <= 1:
            return s
        max_sub_str = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                tmp_str = s[i:j+1]
                if is_palindromic(tmp_str):
                    if len(tmp_str) > len(max_sub_str):
                        max_sub_str = tmp_str
        return max_sub_str

# A Better Search Method


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""

        for i in range(len(s)):
            lo = i
            hi = i
            while hi < len(s) - 1 and s[hi+1] == s[hi]:
                hi += 1

            while lo > 0 and hi < len(s) - 1 and s[lo - 1] == s[hi + 1]:
                lo -= 1
                hi += 1

            if hi - lo + 1 > len(longest):
                longest = s[lo: hi + 1]

        return longest
