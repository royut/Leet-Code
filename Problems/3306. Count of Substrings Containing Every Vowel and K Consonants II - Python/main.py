class Solution(object):
    def countConsonants(self, word):
        return len(word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))

    def checkVowel(self, word):
        if 'a' not in word:
            return False
        if 'e' not in word:
            return False
        if 'i' not in word:
            return False
        if 'o' not in word:
            return False
        if 'u' not in word:
            return False
        return True

    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        substringCount = 0
        start = 0
        end = k+5
        while end <= len(word) and start <= len(word)-k-5:
            tempWord = word[start:end]
            print(tempWord)
            consonants = self.countConsonants(tempWord)
            vowelsCheck = self.checkVowel(tempWord)
            if consonants == k and vowelsCheck:
                substringCount += 1
                for i in range(len(tempWord)):
                    print('infor',i, tempWord[i], end=" ")
                    if tempWord[i] in 'aeiou' and self.checkVowel(tempWord[i:]):
                        substringCount += 1
                    else:
                        break
            if (consonants <= k or not vowelsCheck) and end < len(word):
                end += 1
            else:
                start += 1
            print(substringCount)
        return substringCount


if __name__ == '__main__':
    print('in main')
    word = "ieaouqqieaouqq"
    k = 1
    print(Solution().countOfSubstrings(word, k))
