class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            currentRow = []
            for j in range(len(triangle[i])):
                if j == 0:
                    tempMin = dp[i-1][j]
                elif j == i:
                    tempMin = dp[i-1][j-1]
                else:
                    tempMin = min(dp[i-1][j-1], dp[i-1][j])
                currentRow.append(tempMin + triangle[i][j])
            dp.append(currentRow)
            # print(dp)
        return min(dp[-1])


if __name__ == '__main__':
    print('in main')
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle = [[-10]]
    triangle = [[-1], [2, 3], [1, -1, -3]]
    print(Solution().minimumTotal(triangle))