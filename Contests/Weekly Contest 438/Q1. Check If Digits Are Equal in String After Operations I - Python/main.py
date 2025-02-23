class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            newS = ""
            for i in range(len(s)-1):
                newS = newS + str((int(s[i]) + int(s[i+1])) % 10)
            s = newS
        return s[0] == s[1]


if __name__ == '__main__':
    print('in main')
    print(Solution().hasSameDigits('34789'))
