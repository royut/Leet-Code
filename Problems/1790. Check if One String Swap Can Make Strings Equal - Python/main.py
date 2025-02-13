class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        countUnmatchedLetters = 0
        indexes = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                countUnmatchedLetters += 1
                indexes.append(i)
        if countUnmatchedLetters == 0:
            return True
        elif countUnmatchedLetters == 2:
            if s1[indexes[0]] == s2[indexes[1]] and s1[indexes[1]] == s2[indexes[0]]:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    print('in main')
    s1 = "bank"
    s2 = "kanb"
    print(Solution().areAlmostEqual(s1, s2))
