#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.13%)
# Total Accepted:    281K
# Total Submissions: 736.8K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            temp = b
            b = a
            a = temp

        b = '0' * (len(a) - len(b)) + str(b)


        jinwei = False
        re = ''
        for i,j in zip(a[::-1], b[::-1]):
            temp = int(i) + int(j)
            if jinwei:
                temp += 1
            if temp > 1:
                jinwei = True
                re += str(temp - 2) 
            else:
                jinwei = False
                re += str(temp)
        if jinwei:
            re += '1'
        return re[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary('11', '1'))
