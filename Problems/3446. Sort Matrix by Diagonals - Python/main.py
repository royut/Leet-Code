class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(grid), len(grid[0])  # n: rows, m: columns
        for d in range(n):
            for i in range(n-d):
                for j in range(i+1, n-d):
                    if grid[i+d][i] < grid[j+d][j]:
                        temp = grid[i+d][i]
                        grid[i+d][i] = grid[j+d][j]
                        grid[j+d][j] = temp

        for d in range(1, n):
            for i in range(n-d):
                for j in range(i+1, n-d):
                    if grid[i][i+d] > grid[j][j+d]:
                        temp = grid[i][i+d]
                        grid[i][i+d] = grid[j][j+d]
                        grid[j][j+d] = temp

        return grid


if __name__ == "__main__":
    print('in main')
    grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
    grid = [[0, 1], [1, 2]]
    print(Solution().sortMatrix(grid))