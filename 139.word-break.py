#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (37.07%)
# Likes:    2888
# Dislikes: 158
# Total Accepted:    409.2K
# Total Submissions: 1.1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#
from typing import *
# @lc code=start
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         return self.helper(s, wordDict, 0)
    
#     def helper(self, s, wordDict, start):
#         if start == len(s): # iterate to the end
#             return True
#         for end in range(start+1, len(s)+1):
#             if s[start:end] in wordDict and self.helper(s, wordDict, end):
#                 return True
#         return False
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]


# @lc code=end