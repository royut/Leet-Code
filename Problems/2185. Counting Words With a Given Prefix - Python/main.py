class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        countWords = 0
        for word in words:
            if word[:len(pref)] == pref:
                countWords += 1
        return countWords


if __name__ == '__main__':
    print('in main')
