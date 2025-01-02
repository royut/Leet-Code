class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = ['a', 'i', 'o', 'u', 'e']
        wordsStatus = []
        countWords = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                countWords += 1
                wordsStatus.append(countWords)
            else:
                wordsStatus.append(countWords)
        # print(wordsStatus)
        queriesStatus = []
        for range in queries:
            start, end = range
            if start == 0:
                queriesStatus.append(wordsStatus[end] - 0)
            else:
                queriesStatus.append(wordsStatus[end] - wordsStatus[start - 1])
        return queriesStatus


if __name__ == '__main__':
    print('in main')
    words = ["aba","bcb","ece","aa","e"]
    queries = [[0,2],[1,4],[1,1]]
    print(Solution().vowelStrings(words, queries))