class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        countOccurrence = 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    print('in main')
    haystack = "sadbutsad"
    needle = "sad"
    print(Solution().strStr(haystack, needle))