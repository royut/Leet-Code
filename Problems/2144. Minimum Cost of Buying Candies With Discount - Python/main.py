class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost = sorted(cost)
        minCost = 0
        while len(cost) > 0:
            t1, t2 = cost.pop() if cost else 0, cost.pop() if cost else 0
            minCost += t1 + t2
            if cost: cost.pop()
        return minCost


if __name__ == '__main__':
    print('in main')
    cost = [6, 5, 7, 9, 2, 2]
    cost = [5, 5]
    print(Solution().minimumCost(cost))