class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pre = [-1] * (n+1)
        for i in range(n):
            if i == 0 or s[i-1] == '0':
                pre[i+1] = i
            else:
                pre[i+1] = pre[i]
        # print(pre)
        dominant = 0
        for i in range(1, n+1):
            cnt0 = 1 if s[i-1] == '0' else 0
            j = i
            while j > 0 and cnt0 ** 2 <= n:
                cnt1 = i - pre[j] - cnt0
                # we are checking from pre[j] (index after last zero) to i
                # i - pre[j] is length of the current substring that is being checked
                if cnt0 ** 2 <= cnt1:
                    dominant += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return dominant


if __name__ == "__main__":
    print('in main')
    # s = "00011"
    s = "101101"
    print(Solution().numberOfSubstrings(s))