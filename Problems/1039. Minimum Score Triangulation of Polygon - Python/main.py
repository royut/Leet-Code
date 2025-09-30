from functools import lru_cache


class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        @lru_cache(maxsize=None)
        def rec(x, y):
            print('start', x, y)
            if y-x < 2:
                return 0
            if y-x == 2:
                return values[x] * values[x+1] * values[x+2]
            minScore = float('inf')
            for i in range(x+1, y):
                arr1Val = rec(x, i)
                arr2Val = rec(i, y)
                minScore = min(minScore, values[i] * values[x] * values[y] + arr1Val + arr2Val)
            return minScore
        return rec(0, len(values)-1)


if __name__ == "__main__":
    print("in main")
    values = [1, 3, 1, 4, 1, 5]
    # values = [3, 7, 4, 5]
    # values = [3,8,8,5,9,8,2,2,2]
    print(Solution().minScoreTriangulation(values))