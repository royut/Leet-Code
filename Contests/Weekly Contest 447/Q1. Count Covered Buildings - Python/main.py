class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        vector = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            vector.append(temp)
        rowsFirst = []
        rowsLast = []
        colsFirst = []
        colsLast = []
        for building in buildings:
            vector[building[0]-1][building[1]-1] = 1
        print(vector)
        for i in range(n):
            rowFirst, rowLast = None, None
            colFirst, colLast = None, None
            for j in range(n):
                if vector[i][j] == 1:
                    if rowFirst == None:
                        rowFirst = j
                        rowLast = j
                    else:
                        rowLast = j
                if vector[j][i] == 1:
                    if colFirst == None:
                        colFirst = j
                        colLast = j
                    else:
                        colLast = j
            rowsFirst.append(rowFirst)
            rowsLast.append(rowLast)
            colsFirst.append(colFirst)
            colsLast.append(colLast)
        # print(rowsFirst, rowsLast, colsFirst, colsLast)
        countCoveredBuildings = 0
        for building in buildings:
            i, j = building[0]-1, building[1]-1
            # print(i, j, rowsFirst[i], rowsLast[i], colsFirst[j], colsLast[j])
            try:
                # print(i,j)
                if rowsFirst[i] < j < rowsLast[i] and colsFirst[j] < i < colsLast[j]:
                    countCoveredBuildings += 1
                    # print(True)
            except:
                pass
        return countCoveredBuildings


if __name__ == '__main__':
    print('in main')
    n = 3
    buildings = [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
    # n = 3
    # buildings = [[1, 1], [1, 2], [2, 1], [2, 2]]
    # n = 5
    # buildings = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
    # n = 4
    # buildings = [[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]]
    print(Solution().countCoveredBuildings(n, buildings))
