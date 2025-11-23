class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        sumX = 0
        for char in str(n):
            if int(char) != 0:
                x = x*10 + int(char)
                sumX += int(char)
        return x * sumX


if __name__ == '__main__':
    print('in mian')
    n = 10203004
    print(Solution().sumAndMultiply(n))