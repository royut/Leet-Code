class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        k = 1
        while True:
            x = num1 - k * num2
            xB = bin(x).count('1')
            print(x, xB)
            if x < k:
                return -1
            if xB <= k:
                return k
            k += 1


if __name__ == '__main__':
    print('in main')
    solution = Solution()
    print(solution.makeTheIntegerZero(100, -2))