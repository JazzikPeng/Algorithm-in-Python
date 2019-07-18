
class Solution(object):
    def lengthOfLastWord(self, s):
        if s.strip(): # Get ride of all spaces
            last_word = s.split()[-1]
            return len(last_word)
        else:
            return 0