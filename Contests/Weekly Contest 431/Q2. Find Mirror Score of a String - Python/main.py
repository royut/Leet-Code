class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        charDict = {}
        for char in alphabet:
            charDict[char] = []

        score = 0
        for i in range(len(s)):
            mirror = alphabet[25 - alphabet.find(s[i])]
            # print(i, mirror)
            if charDict[mirror] != []:
                foundIndex = charDict[mirror].pop()
                score += i - foundIndex
            else:
                charDict[s[i]].append(i)
        # print(charDict)

        return score


if __name__ == '__main__':
    print('in main')
    print(Solution().calculateScore('aczzx'))