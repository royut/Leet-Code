class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        if n == 3:
            return values[0] * values[1] * values[2]
        minScore = float('inf')
        for i in range(n):
            for j in range(n):
                if i == 0 and j in [n-1, 0, 1]:
                    continue
                elif i == n-1 and j in [n-2, n-1, 0]:
                    continue
                elif j in [i-1, i, i+1]:
                    continue
                else:
                    # print(i, j)
                    if i < j:
                        arr1 = values[i:j+1]
                        arr2 = values[j:n] + values[0:i+1]
                    else:
                        arr2 = values[j:i+1]
                        arr1 = values[i:n] + values[0:j+1]
                    # print(arr1, arr2)
                    arr1Val = self.minScoreTriangulation(arr1)
                    arr2Val = self.minScoreTriangulation(arr2)
                    minScore = min(minScore, arr1Val + arr2Val)
        return minScore


if __name__ == "__main__":
    print("in main")
    values = [1, 3, 1, 4, 1, 5]
    # values = [3, 7, 4, 5]
    values = [3,8,8,5,9,8,2,2,2]
    print(Solution().minScoreTriangulation(values))