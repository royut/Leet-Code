class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if j > 0 and grid[j][i] <= grid[j - 1][i]:
                    # print('in')
                    count += grid[j - 1][i] - grid[j][i] + 1
                    grid[j][i] = grid[j - 1][i] + 1
                # print(j,i, grid[j][i])
            # print("temp:", count)
        return count


if __name__ == "__main__":
    print("in main")
    grid = [[0],[50]]
    print(Solution().minimumOperations(grid))