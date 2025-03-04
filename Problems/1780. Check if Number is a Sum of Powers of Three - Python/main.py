class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isPowerOfThree = True
        while n > 0:
            if n % 3 == 0:
                n = n // 3
            else:
                n = n - 1
                if n % 3 != 0:
                    isPowerOfThree = False
                    break
        return isPowerOfThree


if __name__ == '__main__':
    print('in main')
    print(Solution().checkPowersOfThree(0))
