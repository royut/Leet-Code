class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        max_profit = 0
        tempo = 0
        for i in range(1, len(prices)):
            # print(prices[i-1], prices[i], diff)
            if prices[i] - prices[i-1] > 0:
                tempo = 1
            if tempo:
                diff += prices[i] - prices[i-1]
                if diff > max_profit:
                    max_profit = diff
            if diff < 0:
                tempo = 0
                diff = 0
        # print(max_profit)
        return max_profit



if __name__ == '__main__':
    print(Solution().maxProfit([7,2,4,1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
