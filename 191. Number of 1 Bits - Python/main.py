class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        countBits = 0
        while n > 1:
            if n % 2 == 1:
                countBits += 1
            n = n // 2
        return countBits + 1


if __name__ == '__main__':
    print('in main')
    print(Solution().hammingWeight(2147483645))