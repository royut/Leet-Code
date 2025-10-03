class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drank = 0
        empty = 0
        full = numBottles
        while empty >= numExchange or full > 0:
            print(full, empty, numExchange, drank)
            if empty < numExchange:
                drank += full
                empty += full
                full = 0
            else:
                empty -= numExchange
                full += 1
                numExchange += 1
            # print(full, empty, numExchange, drank)
        return drank


if __name__ == '__main__':
    print('in main')
    print(Solution().maxBottlesDrunk(13, 6))