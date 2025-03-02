class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper = ""
        lower = ""
        for i in range(len(s)):
            alphabetIndex = alphabet.find(s[i])
            print(alphabetIndex)
            upper = upper + alphabet[alphabetIndex + 1]
            lower = lower + alphabet[alphabetIndex - 1]
        print(alphabet)
        print(s, upper, lower)


if __name__ == '__main__':
    print('in main')
    s = "abced"
    k = 2
    print(Solution().longestPalindromicSubsequence(s, k))
