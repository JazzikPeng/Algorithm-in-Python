class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        if s == "" or s is None:
            return 0
        if len(s) == 1:
            return 1
        len_tracker = []
        queue = []
        length = 0
        for i in s:
            if i in queue:
                length = length - queue.index(i)
                queue = queue[queue.index(i) + 1:]
                queue.append(i)
            else:
                queue.append(i)
                length += 1
            len_tracker.append(length)
        return max(len_tracker)
