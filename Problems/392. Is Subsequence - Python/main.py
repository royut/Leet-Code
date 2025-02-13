class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        counter = 0
        for char in t:
            if char == s[counter]:
                counter += 1
            if counter == len(s):
                return True
        return False


if __name__ == '__main__':
    print(Solution().isSubsequence("abc", "ahbgdc"))