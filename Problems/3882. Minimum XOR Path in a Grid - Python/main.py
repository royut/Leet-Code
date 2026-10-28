class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cost = [[[0 for _ in range(1024)] for _ in range(n)] for _ in range(m)]
        print(grid)
        for i in range(m):
            for j in range(n):
                # print(grid[i][j], end=" ")
                if i == 0:
                    if j == 0:
                        cost[i][j][grid[i][j]] = 1
                    else:
                        for x in range(1024):
                            if cost[i][j-1][x]:
                                cost[i][j][grid[i][j] ^ x] = 1
                else:
                    if j == 0:
                        for x in range(1024):
                            if cost[i-1][j][x]:
                                cost[i][j][grid[i][j] ^ x] = 1
                    else:
                        for x in range(1024):
                            if cost[i-1][j][x]:
                                cost[i][j][grid[i][j] ^ x] = 1
                            if cost[i][j-1][x]:
                                cost[i][j][grid[i][j] ^ x] = 1
        min_cost = float("inf")
        for x in range(1024):
            if cost[m-1][n-1][x] > 0:
                min_cost = min(min_cost, x)
        return min_cost


if __name__ == "__main__":
    print('in main')
    # grid = [[1, 2], [3, 4]]
    # grid = [[6, 7], [5, 8]]
    # grid = [[2, 7, 5]]
    grid = [[26, 24, 3], [2, 22, 17]]
    print(Solution().minCost(grid))