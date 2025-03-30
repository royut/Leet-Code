class Solution(object):
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        minLen1 = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                # print(i, j, j-i, s[j-i:j+1])
                tempS = s[j-i:j+1]
                # print('looking for', tempS[:-1][::-1], tempS[::-1])
                tempT = t.find(tempS[:-1][::-1])
                if tempT == -1:
                    if self.isPalindrome(tempS):
                        minLen1 = len(tempS)
                else:
                    tempT = t.find(tempS[::-1])
                    if tempT == -1:
                        minLen1 = len(tempS) * 2 - 1
                    else:
                        if tempT >= 1:
                            minLen1 = len(tempS) * 2 + 1
                        else:
                            minLen1 = len(tempS) * 2
        minLen2 = 1
        for i in range(1, len(t)):
            for j in range(i, len(t)):
                # print(i, j, j-i, t[j-i:j+1])
                tempT = t[j-i:j+1]
                if self.isPalindrome(tempT):
                    minLen2 = len(tempT)
        return max(minLen1, minLen2)


if __name__ == '__main__':
    print('in main')
    s = "abcde"
    t = "ecdba"
    s = "vn"
    t = "ln"
    print(Solution().longestPalindrome(s, t))