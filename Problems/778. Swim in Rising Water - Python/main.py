class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        low, high = grid[0][0], max(max(row) for row in grid)

        def dfs(row, col, h):
            if row == m - 1 and col == n - 1:
                return True
            seen.add((row, col))
            for diffRow, diffCol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newRow, newCol = row + diffRow, col + diffCol
                if 0 <= newRow < m and 0 <= newCol < n and (newRow, newCol) not in seen and grid[newRow][newCol] <= h:
                    if dfs(newRow, newCol, h):
                        return True
            return False

        while low < high:
            seen = set()
            mid = (low + high) // 2
            if dfs(0, 0, mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    grid = [[0, 2], [1, 3]]
    grid = [[3, 2], [0, 1]]
    # grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(Solution().swimInWater(grid))