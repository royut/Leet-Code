class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        lettersIndex = {}
        for i in range(len(s)):
            if s[i] not in lettersIndex:
                lettersIndex[s[i]] = 1
            else:
                lettersIndex[s[i]] += 1
        # print(lettersIndex)
        countFinalLetters = 0
        for letter in lettersIndex:
            # print(len(lettersIndex[letter]))
            if lettersIndex[letter] % 2 == 1:
                countFinalLetters += 1
            else:
                countFinalLetters += 2
        return countFinalLetters


if __name__ == '__main__':
    print(Solution().minimumLength("azsdadsads"))