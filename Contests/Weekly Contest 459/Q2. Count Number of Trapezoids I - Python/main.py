class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows = {}
        cols = {}
        for point in points:
            y = point[1]
            x = point[0]
            if y in rows:
                rows[y] += 1
            else:
                rows[y] = 1
            if x in cols:
                cols[x] += 1
            else:
                cols[x] = 1

        if len(rows) < len(cols):
            rowsv = []
            for i in rows:
                if rows[i] >= 2:
                    rowsv.append(rows[i] * (rows[i] - 1) // 2)
            total = 0
            for i in range(len(rowsv)):
                for j in range(i+1, len(rowsv)):
                    total += rowsv[i] * rowsv[j]
            return total
        else:
            colsv = []
            for i in cols:
                if cols[i] >= 2:
                    colsv.append(cols[i] * (cols[i] - 1) // 2)
            total = 0
            for i in range(len(colsv)):
                for j in range(i+1, len(colsv)):
                    total += colsv[i] * colsv[j]
            return total


if __name__ == "__main__":
    points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]
    # points = [[0, 0], [1, 0], [0, 1], [2, 1]]
    # points = [[-32,-84],[7,-32],[77,-24],[96,-58]]
    print(Solution().countTrapezoids(points))