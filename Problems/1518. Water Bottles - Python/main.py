class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        r = numBottles
        countDrink = r
        while r >= numExchange:
            exchange = r // numExchange
            countDrink += exchange
            r = exchange + r % numExchange
        return countDrink


if __name__ == '__main__':
    print('in main')
    solution = Solution()
    print(solution.numWaterBottles(9, 4))