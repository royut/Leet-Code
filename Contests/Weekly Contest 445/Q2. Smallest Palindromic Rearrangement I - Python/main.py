class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
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
        if odd is not None:
            ffs += odd
            alphabet[odd] -= 1
        for letter in reversed(alphabetString):
            if letter in alphabet:
                ffs += letter * alphabet[letter]

        return ffs


if __name__ == '__main__':
    print('in main')
    s = "onno"
    print(Solution().smallestPalindrome(s))
