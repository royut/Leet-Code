class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        alphabet = {}
        countOdds = 0
        for char in s:
            if char not in alphabet:
                alphabet[char] = 1
            else:
                alphabet[char] += 1
        for char in alphabet:
            if alphabet[char] % 2 == 1:
                countOdds += 1
        return countOdds <= k <= len(s)


if __name__ == '__main__':
    print('in main')
    print(Solution().canConstruct('true', 2))
