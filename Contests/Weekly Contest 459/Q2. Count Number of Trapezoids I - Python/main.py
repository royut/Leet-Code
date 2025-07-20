class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows = {}
        for point in points:
            y = point[1]
            if y in rows:
                rows[y] += 1
            else:
                rows[y] = 1
        total = 0
        keys = list(rows.keys())
        for i in range(len(rows)):
            ii = keys[i]
            rows_i = rows[ii] * (rows[ii] - 1) // 2
            for j in range(i+1, len(rows)):
                jj = keys[j]
                rows_j = rows[jj] * (rows[jj] - 1) // 2
                # print(rows_i, rows_j)
                total += rows_i * rows_j
        return total


if __name__ == "__main__":
    # points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]
    points = [[0, 0], [1, 0], [0, 1], [2, 1]]
    print(Solution().countTrapezoids(points))