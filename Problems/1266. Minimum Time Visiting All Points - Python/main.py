class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        timeSum = 0
        prev = points[0]
        for i in range(1, len(points)):
            diff = max(abs(points[i][0] - prev[0]), abs(points[i][1] - prev[1]))
            timeSum += diff
            prev = points[i]
        return timeSum


if __name__ == "__main__":
    print('in main')
    points = [[1, 1], [3, 4], [-1, 0]]
    points = [[3, 2], [-2, 2]]
    print(Solution().minTimeToVisitAllPoints(points))