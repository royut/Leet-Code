class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid[0])
        m = len(grid)
        i = 0
        j = 0
        jump = 2
        zigzag = []
        while True:
            # print(j,i, grid[j][i])
            zigzag.append(grid[j][i])
            i += jump
            if i >= n:
                j += 1
                if i == n - 1 + 2:
                    i = n - 2
                elif i == n - 1 + 1:
                    i = n - 1
                jump = -jump
            elif i < 0:
                j += 1
                if i == -2:
                    i = 1
                elif i == -1:
                    i = 0
                jump = -jump
            if j > m - 1:
                break
        return zigzag


if __name__ == '__main__':
    print("in main")
    # grid = [[2,1],[2,1],[2,1]]
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().zigzagTraversal(grid))
