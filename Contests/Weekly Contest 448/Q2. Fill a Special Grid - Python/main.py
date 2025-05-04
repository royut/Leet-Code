class Solution(object):
    def specialGrid(self, N):
        """
        :type N: int
        :rtype: List[List[int]]
        """
        r = 2 ^ N
        qLength = r // 2
        print(qLength)
        grid = [[0 for _ in range(r-1)] for _ in range(r-1)]
        print(grid)


if __name__ == '__main__':
    print('in main')
    print(Solution().specialGrid(1))