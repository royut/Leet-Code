from math import floor


class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        c, v = 0, 0
        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    v += 1
                else:
                    c += 1
        if c > 0:
            return int(floor(v / c))
        else:
            return 0


if __name__ == "__main__":
    print('in main')
    s = "cooear"
    print(Solution().vowelConsonantScore(s))