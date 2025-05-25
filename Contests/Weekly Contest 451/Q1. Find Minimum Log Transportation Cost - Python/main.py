class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if n <= k and m <= k:
            return 0
        cost = 0
        if n > k:
            n -= k
            cost += n * k
        if m > k:
            m -= k
            cost += m * k
        # print(cost)
        return cost


if __name__ == '__main__':
    print('in main')
    print(Solution().minCuttingCost(4, 5, 6))
