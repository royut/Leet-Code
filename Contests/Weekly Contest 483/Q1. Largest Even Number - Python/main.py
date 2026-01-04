class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 0:
                break
        if i == 0:
            if int(s[i]) % 2 == 0:
                return s[i]
            else:
                return ""
        return s[:i+1]
        print(i, s[:i+1])


if __name__ == '__main__':
    s = "1112"
    s = "221"
    s = "1111"
    print(Solution().largestEven(s))