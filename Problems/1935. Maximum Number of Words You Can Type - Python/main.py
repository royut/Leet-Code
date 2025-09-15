class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(" ")
        brokenLetters = set(brokenLetters)
        correctWords = 0
        for word in words:
            brokenFlag = False
            for letter in brokenLetters:
                if letter in word:
                    brokenFlag = True
                    break
            if not brokenFlag:
                correctWords += 1
        return correctWords


if __name__ == '__main__':
    print('in main')
    text = "hello world"
    brokenLetters = "ad"
    print(Solution().canBeTypedWords(text, brokenLetters))