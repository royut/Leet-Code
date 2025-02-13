class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        countPairs = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                # print(words[i], words[j][:len(words[i])], words[j][-len(words[i]):])
                if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                    countPairs += 1
        return countPairs


if __name__ == '__main__':
    print('in main')
    words = ["a","aba","ababa","aa"]
    print(Solution().countPrefixSuffixPairs(words))
