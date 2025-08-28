class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        topRow = n-1
        bottomRow = 0
        for i in range(m):
            foundFlag = False
            for j in range(n):
                if grid[j][i] == 1 and not foundFlag:
                    foundFlag = True
                    if j < topRow:
                        topRow = j
                    if j > bottomRow:
                        bottomRow = j
                elif grid[j][i] == 1:
                    if j > bottomRow:
                        bottomRow = j
        leftCol = m-1
        rightCol = 0
        for i in range(n):
            foundFlag = False
            for j in range(m):
                if grid[i][j] == 1 and not foundFlag:
                    foundFlag = True
                    if j < leftCol:
                        leftCol = j
                    if j > rightCol:
                        rightCol = j
                elif grid[i][j] == 1:
                    if j > rightCol:
                        rightCol = j
        # print(topRow, bottomRow)
        # print(leftCol, rightCol)
        return (bottomRow - topRow + 1) * (rightCol - leftCol + 1)


if __name__ == '__main__':
    print('in main')
    # grid = [[0, 1, 0], [1, 0, 1]]
    grid = [[1, 0], [0, 0]]
    print(Solution().minimumArea(grid))