class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        n = (high - low - 1 + (low % 2 == 0)) // 2 + ((high % 2 == 1) + (low % 2 == 1))
        return n


if __name__ == "__main__":
    print('in main')
    low = 4
    high = 9
    print(Solution().countOdds(low, high))
