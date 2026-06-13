class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        ans = ''
        for word in words:
            weight = 0
            for letter in word:
                # print(letter, alphabet.index(letter))
                weight += weights[alphabet.index(letter)]
            # print(weight)
            ans += alphabet[25 - (weight % 26)]
        return ans


if __name__ == "__main__":
    print('in main')
    words = ["abcd", "def", "xyz"]
    weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
    print(Solution().mapWordWeights(words, weights))