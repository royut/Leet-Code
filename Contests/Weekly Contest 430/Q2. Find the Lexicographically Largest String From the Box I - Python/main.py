class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        maxIndexes = []
        maxLetter = "a"
        for i in range(len(word)):
            if word[i] > maxLetter:
                maxLetter = word[i]
                maxIndexes = [i]
            elif word[i] == maxLetter:
                maxIndexes.append(i)

        # print(maxLetter, maxIndexes)
        i = len(word) - numFriends + 1
        maxWord = ""
        for j in maxIndexes:
            if j + i <= len(word):
                if word[j:j+i] > maxWord:
                    maxWord = word[j:j+i]
            else:
                if word[j:] > maxWord:
                    maxWord = word[j:]
            # print("t: ", word[j:j+i])
        return maxWord


if __name__ == "__main__":
    print("in main")
    print("h" > "g")
    print(Solution().answerString("gh", 1))
