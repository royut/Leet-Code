class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows = {}
        rowsIndex = []
        for point in points:
            y = point[1]
            if y in rows:
                rows[y] += 1
            else:
                rows[y] = 1
                rowsIndex.append(y)
        rowsLineCount = []
        sumEdges = 0
        for row in rows:
            rowsLineCount.append(rows[row] * (rows[row] - 1) // 2)
            sumEdges += rowsLineCount[-1]
        total = 0
        for i in range(len(rowsLineCount)):
            sumEdges -= rowsLineCount[i]
            total += rowsLineCount[i] * sumEdges
        return total % 1000000007


if __name__ == '__main__':
    print('in main')
    points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]
    # points = [[0, 0], [1, 0], [0, 1], [2, 1]]
    print(Solution().countTrapezoids(points))