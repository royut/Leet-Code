class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        n = len(grid[0])  # rows
        m = len(grid)  # cols
        for i in range(m):
            if limits[i] > k:
                limits[i] = k
        # print(limits)
        maxes = []
        for i in range(m):
            if limits[i] != 0:
                grid[i] = sorted(grid[i])
                # print(grid[i], grid[i][-limits[i]:])
                maxes.extend(grid[i][-limits[i]:])
        maxes = sorted(maxes)
        return sum(maxes[-k:])


if __name__ == '__main__':
    print('in main')
    grid = [[1, 2], [3, 4]]
    limits = [1, 2]
    k = 2
    grid = [[5, 3, 7], [8, 2, 6]]
    limits = [2, 2]
    k = 3
    grid = [[0,1]]
    limits = [0]
    k = 0
    print(Solution().maxSum(grid, limits, k))