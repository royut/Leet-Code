class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        m = r - l + 1
        MOD = 10**9 + 7

        prev_up = [1] * m
        prev_down = [1] * m

        for i in range(1, n):
            suf_down = [0] * (m+1)
            pre_up = [0] * (m+1)
            for j in range(m):
                pre_up[j+1] = (pre_up[j] + prev_up[j]) % MOD
            for j in range(m-1, -1, -1):
                suf_down[j] = (suf_down[j+1] + prev_down[j]) % MOD
            # print('ad', prev_down, prev_up)
            # print('add', pre_up, suf_down)
            up = []
            down = []
            for j in range(m):
                up.append(suf_down[j+1] % MOD)
                down.append(pre_up[j] % MOD)
            print(up, down)
            prev_up = up
            prev_down = down

        return (sum(up) + sum(down)) % MOD


if __name__ == "__main__":
    print('in main')
    # n, l, r = 3, 4, 5
    n, l, r = 3, 1, 3
    print(Solution().zigZagArrays(n, l, r))