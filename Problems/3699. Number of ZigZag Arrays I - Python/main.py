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
        pre_fix_sum_up = [0]
        pre_fix_sum_down = [0]
        for i in range(m):
            # down
            dp[0][0][i] = 1
            pre_fix_sum_down.append((pre_fix_sum_down[i] + dp[0][0][i]) % 1000000007)
            # up
            dp[0][1][i] = 1
            pre_fix_sum_up.append((pre_fix_sum_up[i] + dp[0][1][i] % 1000000007))
        # print(dp[0])
        for i in range(1, n):
            npfsu = [0]
            npfsd = [0]
            for j in range(m):
                # make up:
                # print('j up', j, last_arr_up[:j])
                dp[i][0][j] = pre_fix_sum_up[j]
                # make down
                # print('j down', j, last_arr_up[:j])
                dp[i][1][j] = pre_fix_sum_down[-1] - pre_fix_sum_down[j+1]
                npfsd.append((npfsd[j] + dp[i][0][j]) % 1000000007)
                npfsu.append((npfsu[j] + dp[i][1][j]) % 1000000007)
            pre_fix_sum_up = [0]
            pre_fix_sum_down = [0]
            for j in range(m):
                pre_fix_sum_down.append((pre_fix_sum_down[-1] + dp[i][0][j]) % 1000000007)
                pre_fix_sum_up.append((pre_fix_sum_up[-1] + dp[i][1][j]) % 1000000007)
        # print(dp)
        return (pre_fix_sum_down[-1] + pre_fix_sum_up[-1]) % 1000000007


if __name__ == "__main__":
    print('in main')
    # n, l, r = 3, 4, 5
    n, l, r = 3, 1, 3
    print(Solution().zigZagArrays(n, l, r))