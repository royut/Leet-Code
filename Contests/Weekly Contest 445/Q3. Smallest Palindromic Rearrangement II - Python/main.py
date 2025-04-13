class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        alphabetString = 'abcdefghijklmnopqrstuvwxyz'
        alphabet = {}
        for char in s:
            if char in alphabet:
                alphabet[char] += 1
            else:
                alphabet[char] = 1
        odd = None
        ffs = ""
        for letter in alphabetString:
            if letter in alphabet:
                if alphabet[letter] % 2 == 1:
                    odd = letter
                num = alphabet[letter] // 2
                ffs += letter * num
                alphabet[letter] -= num
        # k todo
        # print(ffs[-k])
        if k > 1:
            if len(ffs) < k:
                return ""
            ffs = ffs[:-k] + ffs[-1] + ffs[-k:-2] + ffs[-k]
        temp = ffs[::-1]
        if odd is not None:
            ffs += odd
            alphabet[odd] -= 1
        ffs += temp
        return ffs


if __name__ == '__main__':
    print('in main')
    s = "abba"
    k = 2
    s = "aa"
    k = 2
    s = "bacab"
    k = 1
    print(Solution().smallestPalindrome(s, k))
