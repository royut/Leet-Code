class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (2*n-1)*(2*n-1)-4*(sum(list(range(1, n))))


if __name__ == '__main__':
    print('in main')
    print(Solution().coloredCells(3))
