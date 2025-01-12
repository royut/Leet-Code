class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        n = len(coins[0])
        m = len(coins)
        maxProfits = [[0 for _ in range(n)] for _ in range(m)]
        maxProfits[0][0] = coins[0][0]
        print(maxProfits)
        for i in range(1, n):
            if coins[i][0] >= 0:
                maxProfits[0][i] = maxProfits[0][i - 1] + coins[0][i]

        print(maxProfits)



if __name__ == '__main__':
    print('in main')
    coins = [[0, 1, -1], [1, -2, 3], [2, -3, 4]]
    print(Solution().maximumAmount(coins))
