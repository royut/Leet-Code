class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            b = 1
            bb = 2
            for i in range(3, n+1):
                temp = bb
                bb = bb + b
                b = temp
            return bb


if __name__ == '__main__':
    print(Solution().climbStairs(7))
