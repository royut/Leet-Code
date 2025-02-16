class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        countSameCharacter = 1
        lastChar = s[0]
        for i in range(1, len(s)):
            if s[i] == lastChar:
                countSameCharacter += 1
            else:
                if countSameCharacter == k:
                    return True
                countSameCharacter = 1
            lastChar = s[i]
        if countSameCharacter == k:
            return True
        return False


if __name__ == '__main__':
    print('in main')
    print(Solution().hasSpecialSubstring('abc', 2))