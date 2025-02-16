class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        alphabet = {}
        for i in range(len(s)):
            print(alphabet)
            if s[i] not in alphabet:
                alphabet[s[i]] = 1
            else:
                alphabet[s[i]] += 1
        distinctLetters = 0
        for letter in alphabet:
            if alphabet[letter] == 1:
                distinctLetters += 1
            if distinctLetters >= k:
                return True
        return False


if __name__ == '__main__':
    print('in main')
    print(Solution().maxSubstringLength('azm', 0))
