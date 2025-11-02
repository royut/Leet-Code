class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for wall in walls:
            grid[wall[0]][wall[1]] = 1
        for guard in guards:
            grid[guard[0]][guard[1]] = 2
        # print(grid)
        for guard in guards:
            # check up
            for i in range(guard[0]-1, -1, -1):
                if grid[i][guard[1]] == 1 or grid[i][guard[1]] == 2:
                    break
                grid[i][guard[1]] = 3
            # check down
            for i in range(guard[0]+1, m):
                if grid[i][guard[1]] == 1 or grid[i][guard[1]] == 2:
                    break
                grid[i][guard[1]] = 3
            # check left
            for i in range(guard[1]-1, -1, -1):
                if grid[guard[0]][i] == 1 or grid[guard[0]][i] == 2:
                    break
                grid[guard[0]][i] = 3
            # check right
            for i in range(guard[1]+1, n):
                if grid[guard[0]][i] == 1 or grid[guard[0]][i] == 2:
                    break
                grid[guard[0]][i] = 3
        # print(grid)
        countUnguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    countUnguarded += 1
        return countUnguarded


if __name__ == "__main__":
    print('in main')
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    m = 3
    n = 3
    guards = [[1, 1]]
    walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
    print(Solution().countUnguarded(m, n, guards, walls))