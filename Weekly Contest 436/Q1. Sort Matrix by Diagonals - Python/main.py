class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        for i in range(n):
            for j in range(n-i):
                for k in range(n-i):
                    if grid[i+k][k] < grid[i+j][j]:
                        temp = grid[i+j][j]
                        grid[i+j][j] = grid[i+k][k]
                        grid[i+k][k] = temp
        for i in range(1, n):
            for j in range(n-i):
                for k in range(n-i):
                    if grid[k][i+k] > grid[j][i+j]:
                        temp = grid[j][i+j]
                        grid[j][i+j] = grid[k][i+k]
                        grid[k][i+k] = temp
        return grid


if __name__ == '__main__':
    print('in main')
    grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
    grid = [[1]]
    grid = [[0, 1], [1, 2]]
    print(Solution().sortMatrix(grid))
