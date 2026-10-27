class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = []
        for i in range(m):
            row = ''
            for j in range(n):
                if i == m-1 or j == 0:
                    row += "."
                else:
                    row += "#"
            grid.append(row)
        return grid


if __name__ == "__main__":
    solution = Solution()
    print(solution.createGrid(3, 3))