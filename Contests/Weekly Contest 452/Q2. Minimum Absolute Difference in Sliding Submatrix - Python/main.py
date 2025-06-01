class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        MADArray = []
        for i in range(m-k+1):
            MADRow = []
            for j in range(n-k+1):
                # print(i, j)
                tempSet = set()
                for ii in range(k):
                    for jj in range(k):
                        # print(grid[i+ii][j+jj])
                        tempSet.add(grid[i+ii][j+jj])
                tempSet = sorted(tempSet)
                # print(tempSet)
                if len(tempSet) == 1:
                    tempMin = 0
                else:
                    tempMin = float('inf')
                    for t in range(len(tempSet)-1):
                        if abs(tempSet[t]-tempSet[t+1]) < tempMin:
                            tempMin = abs(tempSet[t]-tempSet[t+1])
                MADRow.append(tempMin)
            MADArray.append(MADRow)
        # print(MADArray)
        return MADArray


if __name__ == '__main__':
    print('in main')
    grid = [[1, -2, 3], [2, 3, 5]]
    k = 2
    grid = [[3, -1]]
    k = 1
    grid = [[1, 8], [3, -2]]
    k = 2
    print(Solution().minAbsDiff(grid, k))