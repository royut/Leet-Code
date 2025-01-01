class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = roman[s[-1]]
        flag = True
        for i in range(len(s) - 2, -1, -1):
            if roman[s[i + 1]] < roman[s[i]]:
                sum += roman[s[i]]
            elif roman[s[i + 1]] > roman[s[i]]:
                sum -= roman[s[i]]
            elif flag:
                sum += roman[s[i]]
            else:
                sum -= roman[s[i]]
        return sum


if __name__ == '__main__':
    print('in main')
    print(Solution().romanToInt('MCMXCIV'))
