class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = False
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ' and not flag:
                flag = True
                here = i + 1
            if s[i] == ' ' and flag:
                return here - i - 1
        return here


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("aawsdasdasd"))