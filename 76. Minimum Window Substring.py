
from collections import *
class Solution:
    # Standard slicing window solution
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1 # Get the val for given key, 0 is not exist

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


    def minWindow1(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for ch in t:
            d[ch] += 1
        i = 0
        count = len(t)
        l, r = 0, float('inf')
        for j, ch in enumerate(s, 1):
            if d[ch] > 0:
                count -= 1
            d[ch] -= 1
            if count == 0:
                while d[s[i]] < 0:
                    d[s[i]] += 1
                    i += 1
                if j - i < r - l:
                    l = i
                    r = j
                d[s[i]] += 1
                i += 1
                count += 1
        return s[l: r] if r != float('inf') else ''

from collections import *
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ''
        dic = Counter(t) # Dictionary of results
        unique_char = len(dic) 
        l, r = 0,0 
        done = 0
        min_win = float('inf')
        
        word_counts = {}
        
        while r < len(s):
            c = s[r]
            word_counts[c] = word_counts.get(c, 0) + 1
            if c in dic and word_counts[c] == dic[c]:
                done += 1
            
            while l < r and done == unique_char:
                c = s[l]
                
                if r - l + 1 < min_win:
                    min_win = r - l + 1
                word_counts[c] -= 1
                if c in dic and word_counts[c] < dic[c]:
                    done -= 1
                l += 1
                
            r += 1
        return "" if min_win == float('inf') else s[l:r+1]
            
        
s = Solution()
S = "aa"
T = "aa"
print(s.minWindow(S, T))
