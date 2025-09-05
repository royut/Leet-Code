class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j or not (points[i][0] <= points[j][0] and points[i][1] >= points[j][1]):
                    continue

                flag = False
                for k in range(len(points)):
                    if k == i or k == j:
                        continue
                    isXContained = (points[k][0] >= points[i][0] and points[k][0] <= points[j][0])
                    isYContained = (points[k][1] <= points[i][1] and points[k][1] >= points[j][1])
                    if isXContained and isYContained:
                        flag = True
                        break
                if not flag:
                    ans += 1
        return ans


if __name__ == "__main__":
    points = [[6, 2], [4, 4], [2, 6]]
    print(Solution().numberOfPairs(points))