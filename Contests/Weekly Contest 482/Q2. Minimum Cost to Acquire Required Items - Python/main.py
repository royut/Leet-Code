class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        if need2 < need1:
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1
        both = need1 * costBoth
        oneBone = (need1 * cost1) + (need1 * cost2)
        currCost = min(both, oneBone)
        remain = need2 - need1
        newBoth = remain * costBoth
        newOneBone = remain * cost2
        currCost += min(newBoth, newOneBone)
        return currCost


if __name__ == '__main__':
    print('in main')
    cost1 = 3
    cost2 = 2
    costBoth = 1
    need1 = 3
    need2 = 2
    cost1 = 5
    cost2 = 4
    costBoth = 15
    need1 = 2
    need2 = 3
    cost1 = 5
    cost2 = 4
    costBoth = 15
    need1 = 0
    need2 = 0
    print(Solution().minimumCost(cost1, cost2, costBoth, need1, need2))