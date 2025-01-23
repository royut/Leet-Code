class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)  # rows
        m = len(grid[0])  # columns
        dictCols = {}
        dictRows = {}
        for i in range(n):
            dictRows[i] = sum(grid[i])
        for i in range(m):
            tempSum = 0
            for j in range(n):
                if grid[j][i] == 1:
                    tempSum += 1
            dictCols[i] = tempSum
        # print(dictRows)
        # print(dictCols)
        countComms = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (dictCols[j] > 1 or dictRows[i] > 1):
                    countComms += 1
        return countComms


if __name__ == '__main__':
    print('in main')
    grid = [[1, 0], [0, 1]]
    # grid = [[1, 0], [1, 1]]
    # grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    grid = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]
    print(Solution().countServers(grid))