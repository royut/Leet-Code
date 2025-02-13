class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sumRow0Front = [grid[0][-1]]
        sumRow1Back = [grid[1][0]]
        n = len(grid[0])
        for i in range(1, n):
            sumRow0Front.append(sumRow0Front[i-1] + grid[0][-i-1])
            sumRow1Back.append(sumRow1Back[i-1] + grid[1][i])
        # print(sumRow0Front, sumRow1Back)
        minSum = sumRow0Front[-1] - grid[0][0]
        for i in range(1, n-1):
            tempSum = max(sumRow0Front[-i-2], sumRow1Back[i-1])
            # print(i, tempSum, sumRow0Front[-i-2] ,sumRow1Back[i-1])
            if tempSum < minSum:
                minSum = tempSum
        if sumRow1Back[-1] - grid[1][-1] < minSum:
            minSum = sumRow1Back[-1] - grid[1][-1]
        # print('in',minSum, minIndex)
        return minSum


if __name__ == '__main__':
    print('in main')
    grid = [[2, 5, 4], [1, 5, 1]]
    grid = [[3, 3, 1], [8, 5, 2]]
    # grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
    # grid = [[20, 3, 20, 17, 2, 12, 15, 17, 4, 15]
    #       , [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]]
    grid = [[1, 2], [1, 2]]
    print(Solution().gridGame(grid))
