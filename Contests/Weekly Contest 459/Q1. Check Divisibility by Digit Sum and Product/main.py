class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = n
        sumDigit = 0
        productDigit = 1
        while n > 0:
            r = n % 10
            sumDigit += r
            productDigit *= r
            n = n // 10
        return m % (sumDigit + productDigit) == 0


if __name__ == '__main__':
    print(Solution().checkDivisibility(99))