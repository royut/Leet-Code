class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # print(sNums, marks)
        score = 0
        for i in range(len(s)):
            # print('i', sNums[i])
            mirror = alphabet[25 - alphabet.find(s[i])]
            found = s[:i].rfind(mirror)
            if found != -1:
                score += i - found
                s = s[:found] + ' ' + s[found+1:]
                s = s[:i] + ' ' + s[i+1:]

        return score


if __name__ == '__main__':
    print('in main')
    print(Solution().calculateScore('abcdef'))
