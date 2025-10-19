class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        vis = [False] * n
        i = 0
        res = s
        s = s + s
        while not vis[i]:
            vis[i] = True
            for j in range(10):
                k_limit = 0 if b % 2 == 0 else 9
                for k in range(k_limit + 1):
                    t = list(s[i:i + n])
                    for odd in range(1, n, 2):
                        t[odd] = str((int(t[odd]) + (j * a)) % 10)
                    for even in range(0, n, 2):
                        t[even] = str((int(t[even]) + (k * a)) % 10)
                    t_str = ''.join(t)
                    if t_str < res:
                        res = t_str
            i = (i + b) % n
        return res


if __name__ == '__main__':
    print('in main')
    s = "5525"
    a = 9
    b = 2
    print(Solution().findLexSmallestString(s, a, b))