class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
        return len(chars.keys())