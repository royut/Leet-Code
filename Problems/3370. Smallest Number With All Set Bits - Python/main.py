class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        powersOfTwo = 1
        while powersOfTwo <= n:
            powersOfTwo *= 2
            # print(powersOfTwo)
        return powersOfTwo - 1


if __name__ == "__main__":
    n = 5
    print(Solution().smallestNumber(n))