class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for char in s:
            if char.isalpha() and char.islower():
                result += char
            elif char == '*':
                if len(result) > 0:
                    result = result[:-1]
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
        return result


if __name__ == '__main__':
    print('in main')
    print(Solution().processStr('a#b%*'))