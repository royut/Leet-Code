class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: (x[0], x[1]))
        # print('base', restrictions)
        prev = restrictions[0]
        for i in range(1, len(restrictions)):
            curr = restrictions[i]
            d = curr[0]-prev[0]
            restrictions[i][1] = min(prev[1]+d, curr[1])
            # print(prev, curr, d)
            prev = curr
        # print('after left to right', restrictions)
        prev = restrictions[-1]
        for i in range(len(restrictions)-2, -1, -1):
            curr = restrictions[i]
            d = prev[0]-curr[0]
            restrictions[i][1] = min(prev[1]+d, curr[1])
            # print(prev, curr, d)
            prev = curr
        # print('after right to left', restrictions)
        prev = restrictions[0]
        maxSoFar = 0
        for i in range(1, len(restrictions)):
            curr = restrictions[i]
            d = curr[0] - prev[0] - abs(prev[1] - curr[1])
            tempMax = max(curr[1] + (d//2), prev[1] + (d//2))
            # print(prev, curr, d, d//2, tempMax)
            if tempMax > maxSoFar:
                maxSoFar = tempMax
            prev = curr
        # edge case for end
        prev = restrictions[-1]
        d = n - prev[0]
        tempMax = prev[1] + d
        if tempMax > maxSoFar:
            maxSoFar = tempMax

        return maxSoFar


if __name__ == "__main__":
    print('in main')
    # n = 5
    # restrictions = [[2, 1], [4, 1]]
    n = 10
    restrictions = [[5, 3], [2, 5], [7, 4], [10, 3]]
    # n = 6
    # restrictions = []
    print(Solution().maxBuilding(n, restrictions))