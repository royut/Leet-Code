class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        m = r - l + 1
        # print(m)
        dp = [[[[] for _ in range(m)], [[] for _ in range(m)]] for _ in range(n)]
        # print(dp)
        for i in range(m):
            # down
            arr = dp[0][0][i]
            dp[0][0][i] = 1
            # up
            arr = dp[0][1][i]
            dp[0][1][i] = 1
        # print(dp[0])
        for i in range(1, n):
            last_arr = dp[i-1]
            # print('iii', i, last_arr)
            # down
            last_arr_down = dp[i-1][0]
            # up
            last_arr_up = dp[i-1][1]
            # print(last_arr_down, last_arr_up)
            for j in range(m):
                # make up:
                # print('j up', j, last_arr_up[:j])
                dp[i][0][j] = sum(last_arr_up[:j])
                # make down
                # print('j down', j, last_arr_up[:j])
                dp[i][1][j] = sum(last_arr_down[j+1:])
        print(dp)
        return (sum(dp[-1][0]) + sum(dp[-1][1])) % 1000000007


if __name__ == "__main__":
    print('in main')
    # n, l, r = 3, 4, 5
    n, l, r = 3, 1, 3
    print(Solution().zigZagArrays(n, l, r))