class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        chasrs = {}
        maxOdd = 0
        minEven = float('inf')
        for char in s:
            if char not in chasrs:
                chasrs[char] = 1
            else:
                chasrs[char] += 1
        for char in chasrs:
            if chasrs[char] % 2 == 0:
                if chasrs[char] < minEven:
                    minEven = chasrs[char]
            else:
                if chasrs[char] > maxOdd:
                    maxOdd = chasrs[char]
        # print(maxEven, maxOdd, minEven, minOdd)
        return maxOdd - minEven


if __name__ == '__main__':
    print('in main')
    print(Solution().maxDifference("mmsmsym"))