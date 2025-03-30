class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        swapCost = []
        minSoFar = float('inf')
        for i in range(len(cost)):
            if cost[i] < minSoFar:
                minSoFar = cost[i]
            swapCost.append(minSoFar)
        return swapCost


if __name__ == '__main__':
    print('in main')
    cost = [1,2,4,6,7]
    print(Solution().minCosts(cost))
