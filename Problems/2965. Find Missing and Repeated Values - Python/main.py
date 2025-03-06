class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        nums = list(range(1, len(grid)*len(grid) + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in nums:
                    nums.remove(grid[i][j])
                else:
                    twice = grid[i][j]
        nums.insert(0, twice)
        return nums


if __name__ == '__main__':
    print('in main')
    grid = [[1, 3], [2, 2]]
    grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    print(Solution().findMissingAndRepeatedValues(grid))
