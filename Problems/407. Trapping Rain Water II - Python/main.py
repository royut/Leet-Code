class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0])
        # print(m, n)
        rMaxesRow = []
        for i in range(n):
            tempArray = [heightMap[0][i]]
            colMax = heightMap[0][i]
            for j in range(1, m-1):
                if heightMap[j][i] < colMax:
                    tempArray.append(0)
                else:
                    colMax = heightMap[j][i]
                    tempArray.append(colMax)
            tempArray.append(heightMap[m-1][i])
            rMaxesRow.append(tempArray)
        print(rMaxesRow)

        rMaxesCol = []
        for i in range(m):
            tempArray = [heightMap[i][0]]
            rowMax = heightMap[i][0]
            for j in range(1, n-1):
                if heightMap[i][j] < rowMax:
                    tempArray.append(0)
                else:
                    rowMax = heightMap[i][j]
                    tempArray.append(rowMax)
            tempArray.append(heightMap[i][n-1])
            rMaxesCol.append(tempArray)
        print(rMaxesCol)

        space = 0
        for i in range(1, m-1):
            rowMax = heightMap[i][0]
            tempSpace = 0
            for j in range(1, n):
                if heightMap[i][j] < rowMax:
                    tempSpace += rowMax - heightMap[i][j]
                else:
                    rowMax = heightMap[i][j]
                    print('in else', i,j-1, heightMap[i][j-1] ,rMaxesRow[j-1][i])
                    if rMaxesRow[j-1][i] == 0:
                        space += tempSpace
                    tempSpace = 0
                # print('space', j, rowMax, tempSpace)
            # print(space)
        return space


if __name__ == '__main__':
    print('in main')
    heightMap = [[1, 4, 2, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    # heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    print(Solution().trapRainWater(heightMap))
