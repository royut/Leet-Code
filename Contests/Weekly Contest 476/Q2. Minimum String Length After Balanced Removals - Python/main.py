class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        :type s: str
        :rtype: int
        """
        countA = 0
        countB = 0
        for char in s:
            if char == "a":
                countA += 1
            elif char == "b":
                countB += 1
        return abs(countA - countB)


if __name__ == '__main__':
    print('in main')
    s = "aaaa"
    print(Solution().minLengthAfterRemovals(s))