class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        spaces = []
        newS = ""
        vowels = "aeiouAEIOU"
        vowelsCount = 0
        tempCount = 0
        reverses = [False]
        countedFlag = False
        for i in range(len(s)):
            if not countedFlag:
                if s[i] in vowels:
                    vowelsCount += 1
            if s[i] == " ":
                spaces.append(i)
                if not countedFlag:
                    countedFlag = True
                    tempCount = 0
                else:
                    reverses.append(tempCount == vowelsCount)
                    tempCount = 0
            elif s[i] in vowels:
                tempCount += 1
        spaces.append(len(s))
        reverses.append(tempCount == vowelsCount)
        # print(spaces, vowelsCount, reverses)
        indexJ = 0
        currFinish = spaces[indexJ]
        currLen = 0
        isReverse = reverses[indexJ]
        for i in range(len(s)):
            if s[i] == " ":
                indexJ += 1
                currFinish = spaces[indexJ]
                currLen = 0
                isReverse = reverses[indexJ]
                newS += " "
            else:
                if isReverse:
                    newS += s[currFinish - currLen - 1]
                    currLen += 1
                else:
                    newS += s[i]
        return newS


if __name__ == "__main__":
    print('in main')
    s = "cat and mice"
    s = "book is nice"
    print(Solution().reverseWords(s))