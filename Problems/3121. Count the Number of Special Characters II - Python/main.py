class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        dictLowers = {}
        dictUppers = {}
        numberOfSpecialChars = 0
        for i in range(len(word)):
            char = word[i]
            if char == char.lower():
                dictLowers[char] = i
            if char == char.upper() and char not in dictUppers:
                dictUppers[char] = i
        for char, i in dictUppers.items():
            if char.lower() in dictLowers and dictLowers[char.lower()] < i:
                numberOfSpecialChars += 1
        return numberOfSpecialChars


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSpecialChars("AbBCab"))