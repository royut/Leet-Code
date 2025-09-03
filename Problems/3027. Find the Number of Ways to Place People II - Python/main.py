import math


class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        for i in range(len(points)):
            for j in range(len(points)):
                if points[i][0] < points[j][0]:
                    tempPoints = points[i]
                    points[i] = points[j]
                    points[j] = tempPoints
                elif points[i][0] == points[j][0] and points[i][1] > points[j][1]:
                    tempPoints = points[i]
                    points[i] = points[j]
                    points[j] = tempPoints

        ans = 0
        for i in range(len(points)):
            A = points[i]
            xMin = A[0] - 1
            xMax = float("inf")
            yMin = float("-inf")
            yMax = A[1] + 1

            for j in range(i + 1, len(points)):
                B = points[j]
                if (
                    xMin < B[0] < xMax
                    and yMin < B[1] < yMax
                ):
                    ans += 1
                    xMin = B[0]
                    yMin = B[1]

        # print(points)
        return ans


if __name__ == "__main__":
    points = [[3, 1], [1, 3], [1, 1]]
    # points = [[6, 2], [4, 4], [2, 6]]
    # points = [[1, 1], [2, 2], [3, 3]]
    print(Solution().numberOfPairs(points))