class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort(key=lambda x: -x)
        coinsSpent = 0
        numBought = 0
        while len(costs) > 0:
            curr = costs.pop()
            if coinsSpent + curr <= coins:
                # print(curr)
                coinsSpent += curr
                numBought += 1
            else:
                break
        return numBought


if __name__ == "__main__":
    print('in main')
    # costs = [1, 3, 2, 4, 1]
    # coins = 7
    costs = [10, 6, 8, 7, 7, 8]
    coins = 5
    costs = [1, 6, 3, 1, 2, 5]
    coins = 20
    print(Solution().maxIceCream(costs, coins))